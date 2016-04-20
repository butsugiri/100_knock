# -*- coding: utf-8 -*-
"""
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
"""
import sys
from gensim.models import Word2Vec
from q86 import WordMatrix
import cPickle as pickle

def load_datasets(fi):
    datasets = []
    for line in fi:
        line = line.rstrip()
        if line == "Word 1,Word 2,Human (mean)":
            continue
        w1,w2,sim = line.split(",")
        datasets.append((w1,w2,sim))
    return datasets

def calc_sim_q85(matrix, word2idx, datasets):
    word_matrix = WordMatrix(matrix, word2idx)
    with open("./data/q94_q85_result.log", "w") as f:
        for data in datasets:
            w1, w2, sim = data
            v1 = word_matrix.word_vector(w1)
            v2 = word_matrix.word_vector(w2)
            guess = word_matrix.cos_sim(v1,v2)
            f.write("{}\t{}\t{}\t{}\n".format(w1,w2,sim,guess))

def calc_sim_q90(model, datasets):
    with open("./data/q94_q90_result.log", "w") as f:
        for data in datasets:
            w1,w2,sim = data
            guess = model.similarity(w1,w2)
            f.write("{}\t{}\t{}\t{}\n".format(w1,w2,sim,guess))

if __name__ == "__main__":
    matrix = pickle.load(open("/work/kiyono/q85_truncated_matrix.pkl"))
    word2idx = pickle.load(open("../80-89/data/q84_word2idx.pkl"))
    model = Word2Vec.load_word2vec_format("./data/wiki_vector.bin", binary=True)
    datasets = load_datasets(sys.stdin)
    calc_sim_q85(matrix,word2idx, datasets)
    calc_sim_q90(model, datasets)
