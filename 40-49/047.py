# -*- coding: utf-8 -*-
"""
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
"""
import sys
from collections import defaultdict

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self,dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def contains(self,pos):
        pos_list = [morph.pos for morph in self.morphs]
        if pos in pos_list:
            return True
        else:
            return False

def return_single_sent():
    sent = []
    for line in sys.stdin:
        line = line.rstrip()
        sent.append(line)
        if line == "EOS":
            yield sent
            sent = []
            continue

def parse_CaboCha_output(inp):
    chunks = []
    new_chunk = None
    for sent in inp:
        for line in sent:
            line = line.rstrip()
            if line.startswith("*"):
                if new_chunk:
                    chunks.append(new_chunk)
                dst = line.split(" ")[2].split("D")[0]
                if dst == "-1":
                    new_chunk = Chunk(None)
                else:
                    new_chunk = Chunk(int(dst))
            elif line =="EOS":
                if new_chunk:
                    chunks.append(new_chunk)
                yield read_kakari_sources(chunks)
                chunks = []
                new_chunk = None
                continue
            else:
                surface, detail = line.split("\t")
                base = detail.split(",")[6]
                pos = detail.split(",")[0]
                pos1 = detail.split(",")[1]
                if pos != "記号": #問題文いわく，記号は含めないこと．
                    new_chunk.morphs.append(Morph(surface,base,pos,pos1))

def read_kakari_sources(chunks): #Chunks[chunks,chunks,...]に係り元の情報を付加する関数
    for n,chunk in enumerate(chunks):
        if chunk.dst:
            dst = chunk.dst
            chunks[dst].srcs.append(n)
    return chunks

def verb_mining(chunks):
    verb_pattern = defaultdict(list)
    def return_left_most_verb(chunk):
        for morph in chunk.morphs:
            if morph.pos == "動詞":
                return morph.base
                break

    for chunk in chunks:
        morphs = chunk.morphs
        #もしサ変接続 + を から構成される文節ならば，係り先を読みにいく
        if len(morphs) == 2 and morphs[0].pos == "名詞" and morphs[0].pos1 == "サ変接続" and morphs[1].surface == "を":
            dst = chunk.dst
            #係り先が動詞ならば，最左の動詞のbaseを返す
            if chunks[dst].contains("動詞"):
                left_most_verb = return_left_most_verb(chunks[dst])
                jutsugo = morphs[0].surface + "を" + left_most_verb
                #動詞に係る述語を探す
                for src_idx in chunks[dst].srcs:
                    for morph in chunks[src_idx].morphs:
                        if morph.pos == "助詞":
                            joshi = morph.surface
                            phrase = "".join([x.surface for x in chunks[src_idx].morphs])
                            verb_pattern[jutsugo].append((joshi,phrase))
    return verb_pattern

if __name__ == "__main__":
    for chunks in parse_CaboCha_output(return_single_sent()):
        verb_pattern = verb_mining(chunks) #defaultdict([])
        for k,v in verb_pattern.iteritems():
            particle = " ".join([t[0] for t in v]) 
            phrase = " ".join([t[1] for t in v])
            print k + "\t" + particle + "\t" + phrase

"""
output
行水を使う	は て が に を	甕は 茂っていたが 茂っていたが 上に 行水を
行水を使う	を	行水を
行水を使う	が に で を	吾輩自身が 代りに 所で 行水を

yieldで一文(chunks block)ごとにやるからこういう出力になる

全部リストに投げてから処理すれば，↑が全部一緒になって出てくるはず
"""
