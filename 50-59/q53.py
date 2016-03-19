# -*- coding: utf-8 -*-
"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

Stanford Core NLPを用いて英文を解析するには:
java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file ../../Dropbox/lab/prog/100_knock/50-59/data/nlp.txt
（公式サイトのコマンドのコピペ）

XPathでは，"//hoge"とすることで，すべてのhoge要素を取得できる
"""
import sys
from lxml import etree

def load_xml(fi):
    tree = etree.parse(fi) #fiで与えたxmlファイルをパース
    for term in tree.xpath("//word"): #XPathで全word要素(単語のsurface)を取得
        sys.stdout.write(term.text + "\n")
    
if __name__ == "__main__":
    with open("./data/out.xml","r") as fi:
        load_xml(fi)
