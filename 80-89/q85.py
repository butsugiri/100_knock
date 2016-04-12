# coding: utf-8

# # q85
# 85 主成分分析による次元圧縮
# 
# 84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．

import sys
from sklearn.decomposition import TruncatedSVD
import cPickle as pickle

q84_matrix = open("./data/q84_matrix.pkl")
matrix = pickle.load(q84_matrix)

svd = TruncatedSVD(300)

# ここで圧縮
new_matrix = svd.fit_transform(matrix)

new_matrix.shape
new_matrix_file = open("/work/kiyono/q85_truncated_matrix.pkl", "w")
pickle.dump(new_matrix, new_matrix_file)
new_matrix_file.close()

