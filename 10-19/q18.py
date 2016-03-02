# -*- coding: utf-8 -*-
"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

SHELL
sort -t $'\t' -k 3,3 -r < data/hightemp.txt

実行例:
python q18.py < data/hightemp.txt
"""
import sys

def main(fi):
    sorted_fi = sorted(fi,key=lambda x:x.split("\t")[2],reverse=True)
    for strm in sorted_fi:
        print strm.rstrip()

if __name__ == "__main__":
    main(sys.stdin)
