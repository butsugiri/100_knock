# -*- coding: utf-8 -*-
"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

SHELL
cat data/hightemp.txt | cut -f 1| sort | uniq -c |sort -r

実行例
python q19.py < data/hightemp.txt
"""
import sys
from collections import defaultdict

def main(fi):
    d = defaultdict(int)
    for line in fi:
        line = line.rstrip()
        col1 = unicode(line.split("\t")[0])
        d[col1] += 1

    for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True):
        print "{}\t{}回".format(k,v)

if __name__ == "__main__":
    main(sys.stdin)
