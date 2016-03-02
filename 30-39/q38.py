# -*- coding: utf-8 -*-
"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""
import sys
import numpy as np #何故numpyが必要なのか? この方が速い?
import matplotlib.pyplot as plt
from collections import defaultdict

def load_freq(fi):
    d = {}
    for line in fi:
        term,freq = line.rstrip().split("\t")
        d[term] = int(freq)
    return d

def create_histogram_input(term_freq):
    hist = []
    for v in term_freq.itervalues():
        hist.append(v)
    return np.array(hist)

def draw_Histogram(inp):
    fig,ax = plt.subplots()
    ax.hist(inp,bins=25,range=(0,50),normed=False,facecolor='g',alpha=0.8)
    ax.set_title("Histogram")
    ax.set_xlabel("出現頻度")
    ax.set_ylabel("Frequency")
    ax.set_ylim(0,200) #適当に設定しないと，頻度1の値が爆発してやばい
    plt.show()

if __name__ == "__main__":
    term_freq = load_freq(sys.stdin)
    hisogram_source = create_histogram_input(term_freq)
    draw_Histogram(hisogram_source)

if __name__ == "__main__":
    freq = load_freq(sys.stdin)
    draw_bargraph(freq)

# output: https://gyazo.com/8e46e0e94d217e8dee1f3273d8adbf60
