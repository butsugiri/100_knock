# -*- coding: utf-8 -*-
"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""
import sys

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def main():
    sent = []
    for line in sys.stdin:
        line = line.rstrip()
        if line.startswith("*"):
            continue
        elif line == "EOS":
            yield sent
            sent = []
            continue
        else:
            surface,detail = line.split("\t")
            base = detail.split(",")[6]
            pos = detail.split(",")[0]
            pos1 = detail.split(",")[1]
            sent.append(Morph(surface,base,pos,pos1))

if __name__ == "__main__":
    for n,sent in enumerate(main()):
        if n == 6: #3文目に対応する
            for morph in sent:
                print morph.surface + "\t" + morph.pos + "\t" + morph.pos1
