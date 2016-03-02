# -*- coding: utf-8 -*-
"""
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
"""
"""
実行例
head -100 data/neko.txt | python 046.py
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

def extract_verb_pattern(chunks):
    verb_pattern = defaultdict(list)
    for chunk in chunks:
        if chunk.contains("動詞"):
            for morph in chunk.morphs:
                if morph.pos == "動詞":
                    predicate = morph.base #述語
            for n in chunk.srcs:
                for morph in chunks[n].morphs:
                    if morph.pos == "助詞":
                        particle = morph.surface
                        phrase = "".join([morph.surface for morph in chunks[n].morphs])
                        verb_pattern[predicate].append((particle,phrase))
    return verb_pattern

if __name__ == "__main__":
    for chunks in parse_CaboCha_output(return_single_sent()):
        verb_pattern = extract_verb_pattern(chunks) #defaultdict([])
        for k,v in verb_pattern.iteritems():
            particle = " ".join([t[0] for t in v]) 
            phrase = " ".join([t[1] for t in v])
            print k + "\t" + particle + "\t" + phrase

