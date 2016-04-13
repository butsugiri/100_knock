# coding: utf-8

"""
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．

usage
python q86.py
"""
import cPickle as pickle
import numpy as np
import argparse
import heapq

class WordMatrix:
    def __init__(self,M, word2idx):
        self.M = M #pickle load済みのmatrix
        self.word2idx = word2idx #wordを受け取ってmatrix用のidxに変換

    def word_vector(self, word):
        # wordを受け取って，idxを読んで，vecを返す
        w_idx = self.word2idx[word]
        return self.M[w_idx]

    def cos_sim(self, v1, v2):
        product = np.linalg.norm(v1) * np.linalg.norm(v2)
        if product == 0:
            return 0
        else:
            return np.dot(v1,v2) / product

    def most_similar_N_vecs(self,v1,N=10):
        """
        vecを受け取り
        cos類似度が高いN termsのタプルが入ったリストを返す
        """
        heap = []
        for word,idx in self.word2idx.iteritems():
            v2 = self.word_vector(word)
            sim = self.cos_sim(v1,v2)
            if len(heap) < N:
                heapq.heappush(heap, (sim, word))
            else:
                heapq.heappushpop(heap, (sim, word))
        heap.sort(key=lambda x: x[0], reverse=True)
        return heap

def main(args):
    matrix = pickle.load(args.matrix)
    word2idx = pickle.load(args.word)
    query = args.input.replace(" ", "_")

    word_matrix = WordMatrix(matrix, word2idx)
    print word_matrix.word_vector(query)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "print word vector")
    parser.add_argument("-m", "--matrix", default="/work/kiyono/q85_truncated_matrix.pkl", type=argparse.FileType("r"))
    parser.add_argument("-w", "--word", default="./data/q84_word2idx.pkl", type=argparse.FileType("r"))
    parser.add_argument("-i", "--input", default="United States", type=str)
    args = parser.parse_args()
    main(args)
