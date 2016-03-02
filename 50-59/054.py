# -*- coding: utf-8 -*-
"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""
from lxml import etree

def main():
    tree = etree.parse("./data/nlp.xml")
    token = tree.xpath("/root/document/sentences/sentence/tokens/token")
    for element in token:
        print "\t".join([x.text for x in element.iter("word","lemma","POS")])

if __name__ == "__main__":
    main()
