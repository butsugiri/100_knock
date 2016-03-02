# -*- coding: utf-8 -*-
"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""
import sys

def load_morph(fi):
    sent = []
    for line in fi:
        line = line.rstrip()
        if line.startswith("EOS"):
            yield sent
            sent = []
        else:
            morph = {}
            sur = unicode(line.split("\t")[0])
            det = line.split("\t")[1].split(",")
            base = unicode(det[6])
            pos = unicode(det[0])
            pos1 = unicode(det[1])
            morph = {"sur":sur, "base":base, "pos":pos, "pos1":pos1}
            sent.append(morph)

if __name__ == "__main__":
    #結果を確認
    #load_morphは後からimportして使う
    for sent in load_morph(sys.stdin):
        for morph in sent:
            for k,v in morph.iteritems():
                print "{}\t{}".format(k,v)
