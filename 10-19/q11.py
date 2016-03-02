# -*- coding: utf-8 -*-
"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

sed -e 's/\t/ /g' < data/hightemp.txt
tr "\t" " " < data/hightemp.txt
expand -t 1 < data/hightemp.txt

実行例:
python 011.py < data/hightemp.txt
"""

import sys

def main(inp):
    for line in inp:
        line = line.rstrip()
        line = " ".join(line.split("\t"))
        print line

if __name__ == "__main__":
    main(sys.stdin)
