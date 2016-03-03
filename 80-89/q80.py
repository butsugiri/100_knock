# -*- coding: utf-8 -*-
"""
トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
空文字列となったトークンは削除
以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．

実行例:
bzcat ./data/enwiki.txt.bz2 |  python q80.py > ./data/stripped_enwiki.txt
"""
import sys

def main(fi):
    for line in fi:
        line = line.strip("\n")
        tokens = [x.strip(".,!?;:()[]'\"") for x in line.split(" ")]
        print " ".join([x for x in tokens if x])

if __name__ == "__main__":
    main(sys.stdin)

