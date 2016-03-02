# -*- coding: utf-8 -*-
"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""
import sys
from stemming.porter2 import stem

def main(inp):
    with open("./data/stop_words.txt","r") as f:
        stop_words = [x.strip() for x in f]

    feature = []
    for line in inp:
        polarity = line.split(" ")[0]
        words = line.split(" ")[1:]
        baseline = []
        for word in words:
            if word in stop_words:
                continue
            else:
                baseline.append(stem(word.strip()))
        feature.append(polarity + " " + " ".join(baseline))
    
    for f in feature:
        print f

if __name__ == "__main__":
    main(sys.stdin)
