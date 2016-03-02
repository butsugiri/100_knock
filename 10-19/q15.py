# -*- coding: utf-8 -*-
"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

tail -10 < data/hightemp.txt

実行例
python 015.py -n 5 < data/hightemp.txt
"""
import sys
import argparse
from collections import deque

def main(inp,n):
    d = deque(sys.stdin,n)
    for line in list(d):
        print line.rstrip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "tail command")
    parser.add_argument('-n', '--N', dest='length', default=5, type=int)
    args = parser.parse_args()
    main(sys.stdin,args.length)
