# -*- coding: utf-8 -*-
"""
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
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

def extract_paths_from_noun(chunks):
    #再帰的にパスを辿る関数 辿れなくなったらおわり
    def return_dst_term(chunk,chunks):
        if chunk.dst:
            return ["".join([x.surface for x in chunk.morphs])] + \
                    return_dst_term(chunks[chunk.dst],chunks)
        else:
            return ["".join([x.surface for x in chunk.morphs])]

    for chunk in chunks:
        if chunk.contains("名詞"):
            output = return_dst_term(chunk,chunks)
            #「名詞句を含む文節単体，係り先なし」を出力しないためにif文で分岐
            if len(output) > 1:
                print " -> ".join(output)

if __name__ == "__main__":
    for chunks in parse_CaboCha_output(return_single_sent()):
        extract_paths_from_noun(chunks)

