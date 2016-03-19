# -*- coding: utf-8 -*-
"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""
import sys
from lxml import etree

def iter_terms(fi):
    tokens = fi.xpath("//token")
    for token in tokens:
        d = {}
        for elem in token.iter("word","lemma","POS"):
            d[elem.tag] = elem.text
        yield d

if __name__ == "__main__":
    with open("./data/out.xml","r") as fi:
        tree = etree.parse(fi)
        for term in iter_terms(tree):
            word = term["word"]
            lemma = term["lemma"]
            pos = term["POS"]
            print "{}\t{}\t{}".format(word,lemma,pos)
