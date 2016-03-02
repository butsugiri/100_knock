# -*- coding: utf-8 -*-
"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．

UNIX:
wc -l < data/hogehoge.txt

実行例:
python 010.py < data/hightemp.txt
"""
import sys

def main(inp):
    lis = [1 for x in inp]
    print len(lis)

if __name__ == "__main__":
    main(sys.stdin)
