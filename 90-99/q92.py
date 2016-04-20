# coding: utf-8
"""
第92問
91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．

今まで100分の1コーパスでやってきましたが，granpaがkey errorを起こすので，諦めて元サイズのコーパスにスイッチしました

usage:
python q92.py

output format:
最初に第9章モデルの予想，次にword2vecの予想
それぞれtab区切りで出力
"""

from gensim.models import Word2Vec
from q86 import WordMatrix
import cPickle as pickle

#重たいモデルのロード
matrix = pickle.load(open("/work/kiyono/q85_truncated_matrix.pkl"))
word2idx = pickle.load(open("../80-89/data/q84_word2idx.pkl"))
model = Word2Vec.load_word2vec_format("./data/wiki_vector.bin", binary=True)

def analogy_q90(w1, w2, w3):
    result = model.most_similar(positive=[w2, w3], negative=[w1], topn=1)
    return result[0]

def analogy_q85(w1, w2, w3):
    # q85で作成したword_matrixと，word2idxをロード (from pickle file)
    word_matrix = WordMatrix(matrix, word2idx)
    
    v1 = word_matrix.word_vector(w1)
    v2 = word_matrix.word_vector(w2)
    v3 = word_matrix.word_vector(w3)
    
    V = v2 - v1 + v3
    
    result = word_matrix.most_similar_N_vecs(V,1) #戻り値は要素一つのリスト
    sim = result[0][0]
    word = result[0][1]
    return (word, sim)

def main():
    # ファイルを読んで，三つ組を用意し，q85とq90で作ったベクトルに投げて，戻り値を回収し，
    # それぞれをファイルの末尾に追記する関数
    with open("./data/q91_family.txt", "r") as f:
        for line in f:
            line = line.rstrip()
            w1,w2,w3,_ = line.split(" ")
            
            q85_vec = analogy_q85(w1,w2,w3)
            q90_vec = analogy_q90(w1,w2,w3)
            
            print "{}\t{}\t{}\t{}\t{}".format(line,q85_vec[0], q85_vec[1],q90_vec[0], q90_vec[1])

if __name__ == "__main__":
    main()

