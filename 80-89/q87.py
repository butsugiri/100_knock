# coding: utf-8

# # q87 単語の類似度
# 85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
import cPickle as pickle
import numpy as np

def cos_sim(v1,v2):
    return np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def main():
    matrix = pickle.load(open("/work/kiyono/q85_truncated_matrix.pkl", "r"))
    word2idx = pickle.load(open("./data/q84_word2idx.pkl", "r"))

    query1 = "United_States"
    query2 = "U.S"

    query1_idx = word2idx[query1]
    query2_idx = word2idx[query2]

    v1 = matrix[query1_idx]
    v2 = matrix[query2_idx]

    print "cos similarity bet. {} and {}: {}".format(query1,query2,cos_sim(v1,v2))

if __name__ == "__main__":
    main()
#output: cos similarity bet. United_States and U.S: 0.83468940146
#苦節3週間，長く苦しい戦いだった
