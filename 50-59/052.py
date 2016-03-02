# -*- coding: utf-8 -*-
"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""
import sys
from stemming.porter2 import stem

def main():
    for line in sys.stdin:
        line = line.rstrip()
        print stem(line)

if __name__ == "__main__":
    main()
