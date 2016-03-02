# -*- coding: utf-8 -*-
"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""
import sys

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base   = base
        self.pos    = pos
        self.pos1   = pos1

    def __repr__(self):
        return "{}\t{},{},{}".format(self.surface,self.base,self.pos,self.pos1)

def load_morph(fi):
    sent = []
    for line in fi:
        line = line.rstrip()
        if line.startswith("*"):
            continue
        elif line == "EOS":
            yield sent
            sent = []
        else:
            sur = unicode(line.split("\t")[0])
            detail = line.split("\t")[1].split(",")
            base = unicode(detail[6])
            pos = unicode(detail[0])
            pos1 = unicode(detail[1])
            sent.append(Morph(sur,base,pos,pos1))

if __name__ == "__main__":
    for n,sent in enumerate(load_morph(sys.stdin)):
        if n == 6:
            for morph in sent:
                print morph
