# -*- coding: utf-8 -*-
"""
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算
そのベクトルと類似度の高い10語とその類似度を出力せよ．
"""
import cPickle as pickle
import argparse
from q86 import WordMatrix

def main(args):
    matrix = pickle.load(args.matrix)
    word2idx = pickle.load(args.word)
    word_matrix = WordMatrix(matrix, word2idx)

    v1 = word_matrix.word_vector("Spain")
    v2 = word_matrix.word_vector("Madrid")
    v3 = word_matrix.word_vector("Athens")
    
    V = v1 - v2 + v3
    result = word_matrix.most_similar_N_vecs(V)

    for sim, word in result:
        print "{}\t{}".format(word, sim)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "print word vector")
    parser.add_argument("-m", "--matrix", default="/work/kiyono/q85_truncated_matrix.pkl", type=argparse.FileType("r"))
    parser.add_argument("-w", "--word", default="./data/q84_word2idx.pkl", type=argparse.FileType("r"))
    parser.add_argument("-i", "--input", default="England", type=str)
    parser.add_argument("-n", "--number", default=10, type=int)
    args = parser.parse_args()
    main(args)

#output: https://gyazo.com/1456265d3328ea1df5929288c9320730
