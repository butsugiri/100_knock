# -*- coding: utf-8 -*-
"""
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
"""
import sys

def main(fi):
    q85 = 0 #正答数 for q85 matrix
    q90 = 0 #正答数 for word2vec
    for n, line in enumerate(fi):
        elems = line.rstrip().split()
        true_ans = elems[3]
        q85_ans = elems[4]
        q90_ans = elems[6]

        if true_ans == q85_ans:
            q85 += 1
        if true_ans == q90_ans:
            q90 += 1

    print "q85 model: {} / {} = {}".format(q85, n, q85*1.0/n)
    print "q90 model: {} / {} = {}".format(q90, n, q90*1.0/n)

if __name__ == "__main__":
    main(sys.stdin)

"""
~/work/nlp100/90-99 kiyono@charanda02 (sandbox)
❯ python q93.py < data/q92_result.log
q85 model: 29 / 505 = 0.0574257425743
q90 model: 307 / 505 = 0.607920792079
"""