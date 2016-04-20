# -*- coding: utf-8 -*-
"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from q36 import count_terms

def draw_bargraph(term_freq):
    N = 10
    freq = []
    label = []
    for k,v in sorted(term_freq.items(), key = lambda x:x[1],reverse = True):
        freq.append(v)
        label.append(k)
    ind = np.arange(N)
    width = 1.00

    fig, ax = plt.subplots()
    rects = ax.bar(ind,tuple(freq[0:10]), width,color='r')
    ax.set_ylabel("頻度")
    ax.set_title("頻出単語 in 吾輩は猫である")
    ax.set_xticks(ind+0.5)
    ax.set_xticklabels(tuple(label[0:10]))
    plt.show()

if __name__ == "__main__":
    freq = count_terms(sys.stdin)
    draw_bargraph(freq)

# output: https://gyazo.com/94292f219d69ad6124abb69d57dc1d16
