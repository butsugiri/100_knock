# -*- coding: utf-8 -*-
"""
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
"""
import cPickle as pickle
import heapq
from q87 import cos_sim

def main():
    word_matrix = pickle.load(open("/work/kiyono/q85_truncated_matrix.pkl", "r"))
    word2idx = pickle.load(open("./data/q84_word2idx.pkl", "r"))

    query = "England"
    query_idx = word2idx[query]
    query_vec = word_matrix[query_idx]

    heap = []
    for word,idx in word2idx.iteritems():
        vec = word_matrix[idx]
        similarity = cos_sim(query_vec, vec)
        if len(heap) < 10:
            heapq.heappush(heap, (similarity, word))
        else:
            heapq.heappushpop(heap, (similarity,word))
    
    sort_result = []
    while heap:
        sort_result.append(heapq.heappop(heap))
    sort_result.reverse()

    for similarity, word in sort_result:
        print "{}\t{}".format(word, similarity)

if __name__ == "__main__":
    main()
