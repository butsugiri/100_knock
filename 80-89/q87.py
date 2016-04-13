# coding: utf-8

"""
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．

usage
python q87.py
"""
import cPickle as pickle
import argparse
from q86 import WordMatrix #クラス

def main(args):
    matrix = pickle.load(args.matrix)
    word2idx = pickle.load(args.word)

    query1 = "United_States"
    query2 = "U.S"

    word_matrix = WordMatrix(matrix, word2idx)
    v1 = word_matrix.word_vector(query1)
    v2 = word_matrix.word_vector(query2)
    similarity = word_matrix.cos_sim(v1,v2)
    print "cos similarity bet. {} and {}: {}".format(query1,query2,similarity)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "print word vector")
    parser.add_argument("-m", "--matrix", default="/work/kiyono/q85_truncated_matrix.pkl", type=argparse.FileType("r"))
    parser.add_argument("-w", "--word", default="./data/q84_word2idx.pkl", type=argparse.FileType("r"))
    args = parser.parse_args()
    main(args)
#output: cos similarity bet. United_States and U.S: 0.83468940146
#苦節3週間，長く苦しい戦いだった...
