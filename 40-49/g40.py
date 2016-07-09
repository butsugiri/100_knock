# -*- coding: utf-8 -*-
"""
#40をgroupbyを使ってスゥマートに解き直してみた
"""
import sys
from itertools import groupby

class Morph(object):
# Morphのコンストラクタにlineをそのまま渡せたほうが便利じゃん？
    def __init__(self, line):
        line = line.rstrip()
        self.sur = unicode(line.split("\t")[0])
        detail = line.split("\t")[1].split(",")
        self.base = unicode(detail[6])
        self.pos = unicode(detail[0])
        self.pos1 = unicode(detail[1])

    def __str__(self):
        return "{}\t{} {} {}".format(self.sur,self.base,self.pos,self.pos1)

class Line(object):
#クラス変数の定義 != インスタンス変数
#名前を付けるノリ
    EOS = 0
    CHUNK = 1
    MORPH = 2
 
def classify_cabocha_line(line):
    if line == 'EOS\n':
        return Line.EOS
    elif line.startswith('* '):
        return Line.CHUNK
    else:
        return Line.MORPH

def extract_mecab_list(fi):
    for startswith_eos, sections in groupby(fi, key=lambda l: l=="EOS\n"):
        output = []
        if not startswith_eos:
            for _type, section in groupby(sections, key=classify_cabocha_line):
                if _type == Line.MORPH:
                    output += [Morph(line) for line in section]
            yield output

if __name__ == "__main__":
    for n, mecabs in enumerate(extract_mecab_list(sys.stdin)):
        if n == 3:
            for m in mecabs:
                print m
            break

