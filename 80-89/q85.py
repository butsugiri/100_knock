# coding: utf-8

"""
85 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．

usage
python q85.py
"""

import sys
from sklearn.decomposition import TruncatedSVD
import cPickle as pickle

with open("./data/q84_matrix.pkl") as q84_matrix, open("/work/kiyono/q85_truncated_matrix.pkl", "w") as new_matrix_file:
    matrix = pickle.load(q84_matrix)
    svd = TruncatedSVD(300)
# ここで圧縮
    new_matrix = svd.fit_transform(matrix)
# 圧縮後の行列を保存 注:new_matrixはこの時点ですごく大きいnumpyの行列になっている
    pickle.dump(new_matrix, new_matrix_file)
