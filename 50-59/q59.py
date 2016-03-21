# -*- coding: utf-8 -*-
"""
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

nltkのtreeモジュールを使うとさっぱりと書ける
http://www.nltk.org/api/nltk.html#nltk.tree.Tree
他にもs expression parserはあるみたいだけど…
"""
from nltk.tree import Tree
from lxml import etree

def main(tree):
    NPs = set()
    parses = tree.xpath("//parse")
    for parse in parses:
        s_exps = Tree.fromstring(parse.text)
        for subtree in s_exps.subtrees():
            if subtree.label() == "NP":
                NP = " ".join(subtree.leaves())
                NPs.add(NP)

    for NP in list(NPs):
        print NP

if __name__ == "__main__":
    with open("./data/out.xml","r") as fi:
        tree = etree.parse(fi)
        main(tree)
