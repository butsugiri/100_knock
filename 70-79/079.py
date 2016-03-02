# -*- coding: utf-8 -*-
"""
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．

+1 -1 0.38388.....
を読んでなんとやら
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from mod077 import calc_score

def main():
    positive = []
    negative = []
    with open("./classified.log","r") as f:
        for line in f:
            line = line.strip()
            label = line.split("\t")[0]
            prob = float(line.split("\t")[2])
            if label == "+1": #正例の場合
                positive.append(prob)
            else:
                negative.append(prob)
    np_positive = np.array(positive)
    np_negative = np.array(negative)
    threshold = np.arange(0,1,0.1)

    precision = []
    recall = []
    for t in threshold:
        tp = len(np_positive[np_positive>=t])
        tn = len(np_negative[np_negative<=t])
        fp = len(np_negative[np_negative > t])
        fn = len(np_positive[np_positive < t])
        precision.append(tp / float(tp + fp))
        recall.append(tp / float(tp + fn))

    fig,ax = plt.subplots()
    ax.plot(recall,precision)
    ax.set_title("PR Curve")
    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")
    ax.grid()
    plt.show()

if __name__ == "__main__":
    main()
