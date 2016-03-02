# -*- coding: utf-8 -*-
"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""
import sys
from lxml import etree

def main():
    tree = etree.parse("./data/nlp.xml")
    token = tree.xpath("/root/document/sentences/sentence/tokens/token/word")
    for word in token:
        print word.text

if __name__ == "__main__":
    main()
