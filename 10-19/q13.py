# -*- coding: utf-8 -*-
"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

pasteコマンドの場合
paste data/col1.txt data/col2.txt

実行例
python 013.py
"""
import sys

def main():
    f1 = open("./data/col1.txt", "r")
    f2 = open("./data/col2.txt", "r")

    for col1,col2 in zip(f1,f2):
        col1 = col1.rstrip()
        col2 = col2.rstrip()
        print "%s\t%s" % (col1, col2)

if __name__ == "__main__":
    main()
