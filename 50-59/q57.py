# -*- coding: utf-8 -*-
"""
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．

記号（カンマなど）の取り扱いがイマイチ分からず…
係り受けの図に含めても良いものか．

実行例
python q57.py | dot -Tpng -o hogehoge.png
https://gyazo.com/53df0b44496b11d36be2bc0f4f1ed996
"""
import sys
from lxml import etree

class Dependency:
    def __init__(self):
        self.word2idx = {}
        self.edges = []

def create_edges(tree):
    """
    一度out.xmlをすべて舐めて，全体についてdependencyを
    Dependencyのインスタンスのリストにまとめている
    """
    coll_deps = tree.xpath("//dependencies[@type='collapsed-dependencies']")
    deps_lis = []
    for n, coll_dep in enumerate(coll_deps):#coll_depで1sentence
        deps = Dependency()
        for dep in coll_dep.iter("dep"):
            src_idx = dep.find("governor").get("idx")
            src_txt = dep.find("governor").text
            dst_idx = dep.find("dependent").get("idx")
            dst_txt = dep.find("dependent").text
            deps.word2idx[src_txt] = src_idx
            deps.word2idx[dst_txt] = dst_idx
            deps.edges.append((src_idx,dst_idx))
        deps_lis.append(deps)
    return deps_lis

def gen_dotlang(deps,digraph = True):
    """
    dependencyのインスタンスを受け取りdot言語として出力
    """
    header = "digraph hogehoge" if digraph else "graph hugahuga"
    sep = " -> " if digraph else " -- "

    print header + "{"
    print "\t//label of nodes..."
    #idx [label]としておかないと，graphvizのsyntax error
    #(,とか-はそのままノードにできない…)
    for idx,label in deps.word2idx.iteritems():
        print '\t{} [label="{}"];'.format(label,idx)
    print "\n\t//node dependencies..."
    for edge in deps.edges:
        print "\t{};".format(sep.join(edge))
    print "}"

if __name__ == "__main__":
    with open("./data/out.xml","r") as fi:
        tree = etree.parse(fi)
        deps_lis = create_edges(tree)
        gen_dotlang(deps_lis[1])
