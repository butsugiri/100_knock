# -*- coding: utf-8 -*-
"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． 
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""
import sys
from stemming.porter2 import stem

def main(fi):
    for word in fi:
        word = word.rstrip()
        print stem(word)

if __name__ == "__main__":
    main(sys.stdin)
