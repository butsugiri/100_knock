# -*- coding: utf-8 -*-
"""
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
"""
import cPickle as pickle
import argparse
from q86 import WordMatrix

def main(args):
    matrix = pickle.load(args.matrix)
    word2idx = pickle.load(args.word)
    word_matrix = WordMatrix(matrix, word2idx)
    query = "England"
    vec = word_matrix.word_vector(query)
    results = word_matrix.most_similar_N_vecs(vec, 10)
    for similarity, word in results:
        print "{}\t{}".format(word, similarity)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "print word vector")
    parser.add_argument("-m", "--matrix", default="/work/kiyono/q85_truncated_matrix.pkl", type=argparse.FileType("r"))
    parser.add_argument("-w", "--word", default="./data/q84_word2idx.pkl", type=argparse.FileType("r"))
    parser.add_argument("-i", "--input", default="England", type=str)
    args = parser.parse_args()
    main(args)

