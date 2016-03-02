# -*- coding: utf-8 -*-
"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

cutコマンドを使うと:
cut -f 1 < data/hightemp.txt で一行目
cut -f 2 < data/hightemp.txt で二行目

実行例
python 012.py < data/hightemp.txt
"""
import sys

def main(inp):
    col1 = open("./data/col1.txt", "w")
    col2 = open("./data/col2.txt", "w")
    for line in inp:
        line = line.rstrip()
        columns = line.split("\t")
        col1.write(unicode(columns[0]) + "\n")
        col2.write(unicode(columns[1]) + "\n")
    col1.close()
    col2.close()

if __name__ == "__main__":
    main(sys.stdin)
