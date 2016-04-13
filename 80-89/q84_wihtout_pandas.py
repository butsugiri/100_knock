# coding: utf-8

"""
84: 単語文脈行列の作成
83の出力を利用し，単語文脈行列Xを作成せよ

使ったライブラリなど
scipy.sparse: 疎行列を扱うためのライブラリ
cPickle: pickleのC実装．pickleよりもいくらか速い．cPickleのデメリット(サブクラス化できないとかなんとか)は理解していない．

方針
    * q83で作成したf(t,c), f(t,*), f(*,c)らのtxtファイルをロードする．それぞれを辞書に格納．
    * 疎行列のインデックスにwordを直接利用することはできないため，word_setを作ってからwordからidxに変換する辞書を作成する．（これは後にpickle化する）
    * 問に与えられたPPMIの定義に沿って，疎行列に値を格納していく．0な値を作らないとかいうのは，疎行列のライブラリがうまくやってくれるはず．（値を挿入するまでは行列はメモリ上に展開されない，という雑な理解）
    * 最後にcPickleを使って保存

usage
python q84.py
"""

import sys
import cPickle
import numpy as np
import scipy.sparse as sp
from collections import defaultdict

tc_freq = defaultdict(int)
xc_freq = {}
tx_freq = {}
word_set = set()

with open("/work/kiyono/f_tc.txt", "r") as tc_file, 
     open("/work/kiyono/f_c.txt", "r") as xc_file, 
     open("/work/kiyono/f_t.txt", "r") as tx_file:

    for line in tc_file:
        target,context,count = line.rstrip().split("\t")
        tc_freq[(target,context)] = int(count)
    N = len(tc_freq)

    for line in xc_file:
        word,freq = line.rstrip().split("\t")
        word_set.add(word)
        xc_freq[word] = int(freq)

    for line in tx_file:
        word, freq = line.rstrip().split("\t")
        tx_freq[word] = int(freq)

    word2idx = {}
    for n, word in enumerate(word_set):
        word2idx[word] = n

matrix = sp.lil_matrix((len(word2idx), len(word2idx)))

print "N is {}".format(N)

for word,count in tc_freq.iteritems():
    target = word[0]
    context = word[1]
# f(t,c)が10以上の場合にのみPPMIを計算すればよい
    if count >= 10:
        t_idx = word2idx[target]
        c_idx = word2idx[context]
        matrix[t_idx,c_idx] = max(np.log10((N*count) * 1.0 / (xc_freq[context] * tx_freq[target] * 1.0)) , 0)
    # else:
    #     pass

word_idx_file = open("./data/q84_word2idx.pkl", "w")
cPickle.dump(word2idx, word_idx_file)
word_idx_file.close()

matrix_file = open("./data/q84_matrix.pkl", "w")
cPickle.dump(matrix, matrix_file)
matrix_file.close()

# pickle化したファイルをcloseするのを忘れた結果，後に利用するときにEOF errorとかが出たので注意
