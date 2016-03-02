# -*- coding: utf-8 -*-
"""
74. 予測
73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．

実行例
python 074.py model_baseline.txt "this movie sucks and it's worst"
ここでmodel_baseline.txtはclassiasで学習したモデル
"""
import sys
from math import exp
from stemming.porter2 import stem

def extract_feature(sent):
    with open("./data/stop_words.txt","r") as f:
        stop_words = [x.strip() for x in f]
    features = []
    words = sent.split(" ")
    for word in words:
        if word in stop_words:
            continue
        else:
            features.append(stem(word.strip()))
    return features

def load_model(fi):
    model = {}
    with open(fi,"r") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("@classias"):
                continue
            else:
                weight_str = line.split("\t")[0]
                feature = line.split("\t")[1]
                if feature == "__BIAS__":
                    bias = float(weight_str)
                else:
                    model[feature] = float(weight_str)
    return (model,bias)

def classify_polarity_and_probability(model,bias,sent):
    features = extract_feature(sent)
    weight = 0.0
    for feature in features:
        if feature in model:
            weight += model[feature]
    weight_sum = weight + bias
    if weight_sum < 0.0:
        polarity = "-1"
    else:
        polarity = "+1"
    prob = 1.0 / (1.0 + exp(-1.0 * weight_sum))

    print "{} Probability: {}".format(polarity,prob)

if __name__ == "__main__":
    model_file = sys.argv[1]
    sent = sys.argv[2]
    model, bias = load_model(model_file)
    classify_polarity_and_probability(model,bias,sent)
