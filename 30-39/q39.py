# -*- coding: utf-8 -*-
"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def load_freq(fi):
    d = {}
    for line in fi:
        term,freq = line.rstrip().split("\t")
        d[term] = int(freq)
    return d

def draw_logscale_graph(inp):
#data_sourceなタプルつくる
    x_dataSet = []
    y_dataSet = []
    for k,v in sorted(inp.items(),key=lambda x:x[1],reverse=True):
        x_dataSet.append(k)
        y_dataSet.append(v)
    x = np.arange(0,len(x_dataSet),1)
    y = tuple(y_dataSet)

#こっからプロット
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("単語の出現頻度順位")
    ax.set_ylabel("出現頻度")
    ax.set_title("039.py - Zipfの法則")
    ax.set_yscale("log")
    ax.set_xscale("log")
    ax.plot(x,y,"ro")
    plt.show()

if __name__ == "__main__":
    term_freq = load_freq(sys.stdin)
    draw_logscale_graph(term_freq)

# https://gyazo.com/ac748a7746d2a706f7dbc185692f3a84
