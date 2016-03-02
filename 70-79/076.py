# -*- coding: utf-8 -*-
"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．

実行例
python 076.py model_baseline.txt < ./data/sentiment.txt
"""
import sys
from math import exp
from stemming.porter2 import stem

def extract_feature(sent):
    with open("./data/stop_words.txt","r") as f:
        stop_words = [x.strip() for x in f]
    features = []
    for word in sent:
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

def classify(model,bias,sent):
    features = extract_feature(sent)
    weight = 0.0
    for feature in features:
        if feature in model.keys():
            weight += model[feature]
    weight_sum = weight + bias
    if weight_sum < 0.0:
        polarity = "-1"
    else:
        polarity = "+1"
    prob = 1.0 / (1.0 + exp(-1.0 * weight_sum))
    return polarity, prob

if __name__ == "__main__":
    sys.stderr.write("Correct Label\tPredicted Label\tProbability")
    model_file = sys.argv[1]
    model, bias = load_model(model_file)
    for line in sys.stdin:
        line = line.strip()
        label = line.split(" ")[0]
        sent = line.split(" ")[1:]
        label_predict, prob = classify(model,bias,sent)
        print "%s\t%s\t%s" % (label,label_predict,prob)

