# coding: utf-8

# # q86
# 86 単語ベクトルの表示
# 85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．

import sys
import cPickle as pickle

matrix_file = open("/work/kiyono/q85_truncated_matrix.pkl", "r")
matrix = pickle.load(matrix_file)
matrix_file.close()

word2idx = pickle.load(open("./data/q84_word2idx.pkl", "r"))

query = "United_States"
query_idx = word2idx[query]

print matrix[query_idx]

