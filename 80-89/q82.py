# -*- coding: utf-8 -*-
"""
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．
ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
"""
import sys
from random import randint

window = 5

def extract_context(tokens):
    for n,token in enumerate(tokens):
        width = randint(1,window)
        for m in xrange(max(0,n-width),min(len(tokens),width+n)):
            if m == n:
                continue
            else:
                yield token,tokens[m]

def main(fi):
    for line in fi:
        tokens = line.rstrip().split()
        for t,c in extract_context(tokens):
            print "{}\t{}".format(t,c)


if __name__ == "__main__":
    main(sys.stdin)
