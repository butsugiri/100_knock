# -*- coding: utf-8 -*-
"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい

実行例
❯ cat data/neko.txt.cabocha | awk "NR==26,NR==43" | python q44.py
例の文をまた使いました
"""
import sys
import pydot
from q41 import gen_chunks

def edges(chunks):
    edges = []
    for chunk in chunks:
        if chunk.dst:
            dst = chunk.dst
            dst_txt = unicode(chunks[dst].chunk2str())
            src_txt = unicode(chunk.chunk2str())
            if dst_txt != "" and src_txt != "":
                edges.append((src_txt,dst_txt))
    return edges

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        edges = edges(chunks)
        n = pydot.Node('node')
        n.fontsize = 9
        #(src,dst)のタプルを要素として持つlistを与えればよい
        g = pydot.graph_from_edges(edges, directed = True)
        g.add_node(n)
        g.write_jpeg("./data/graph.jpg", prog='dot')

# https://gyazo.com/b938524cf208126f472d757cd50a6d69
