# -*- coding: utf-8 -*-
"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

UNIX
cut -f 1 < data/hightemp.txt | sort | uniq

実行例
python 017.py < data/hightemp.txt
"""
import sys

def main(inp):
    s = set()
    for line in inp:
        line = unicode(line).rstrip()
        col_1 = line.split("\t")[0]
        s.add(col_1)

    for l in list(s):
        print l

if __name__ == "__main__":
    main(sys.stdin)
