# -*- coding: utf-8 -*-
"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

head -N ./data/hightemp.txt

実行例
python 014.py -n 10 < data/hightemp.txt
"""
import sys
import argparse

def main(inp,n):
    for line,n in zip(inp,range(n)):
        print line.rstrip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "head command")
    parser.add_argument('-n', '--N', dest='length', default=5, type=int)
    args = parser.parse_args()
    main(sys.stdin,args.length)
