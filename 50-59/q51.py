# -*- coding: utf-8 -*-
"""
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

シェルでやるなら
python q50.py < data/nlp.txt | sed 's/ /\n/g'
"""
import sys

def main(fi):
    for line in fi:
        line = line.rstrip()
        words = line.split()
        for word in words:
            print word
        print

if __name__ == "__main__":
    main(sys.stdin)
