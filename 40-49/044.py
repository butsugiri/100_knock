# -*- coding: utf-8 -*-
"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

"""
入力としては
sed -n '開始行,終了行p' data/neko.txt | cabocha -f1 | python 044.py

"""
import sys
import pydot

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

def return_edges(chunks):
    edges = []
    for chunk in chunks:
        dst = chunk.dst
        if dst:
            dst_txt = "".join([x.surface for x in chunks[dst].morphs])
            src_txt = "".join([x.surface for x in chunk.morphs])
            edges.append((unicode(src_txt),unicode(dst_txt)))
    return edges

if __name__ == "__main__":
    for chunks in parse_CaboCha_output(return_single_sent()):
        edges = return_edges(chunks)
        n = pydot.Node('node')
        n.fontsize = 9
        g = pydot.graph_from_edges(edges, directed = True)
        g.add_node(n)
        g.write_jpeg("graph.jpg", prog='dot')
