# -*- coding: utf-8 -*-
"""
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．
ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．

usage:
bzcat ./data/enwiki.txt.bz2 |  python q80.py | python q81.py| python q82.py
"""
import sys
from random import randint

window = 5

def extract_context(tokens):
    for n,token in enumerate(tokens):
        width = randint(1,window)
        contexts = []
        for m in xrange(max(0,n-width),min(len(tokens),width+n)):
            if m == n:
                continue
            else:
                contexts.append(tokens[m])
        yield token, "\t".join(contexts)
        contexts = []

def main(fi):
    for line in fi:
        tokens = line.rstrip().split()
        for t,c in extract_context(tokens):
            if c:
                print "{}\t{}".format(t,c)
"""
出力時のフォーマットとしては
target  context1    context2    context3....
とタブ区切りで出力

当初，
target context1
target context2
hogehoge
と出力していた．
結果，
f(t,*)を"len(context)-1"回余分にカウントしてしまい，
文脈行列がよくわからないことになった．
"""

if __name__ == "__main__":
    main(sys.stdin)
