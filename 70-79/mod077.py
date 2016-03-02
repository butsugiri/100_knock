# -*- coding: utf-8 -*-
"""
077.pyの改変版

"""
import sys

def calc_score(inp,threshold=0.5):
    tp = 0.0 # 正例と判定された正例
    tn = 0.0 # 負例と判定された負例
    fp = 0.0 # 正例と判定された負例
    fn = 0.0 # 負例と判定された正例

    for line in inp:
        line = line.strip()
        actual,label,prob = line.split("\t")
        if threshold > float(prob):
            label = "-1"
        else:
            label = "+1"
        if actual == label: #正解パターン
            if label == "+1":
                tp += 1
            else:
                tn += 1
        else: #不正解パターン
            if label == "-1":
                fn += 1
            else:
                fp += 1
    accuracy = (tp+tn) / (tp+tn+fp+fn)
    #precision: percentage of selected items that are correct
    precision = tp/(tp+fp)
    #recall: percentage of correct items that are selected
    recall = tp/(tp+fn)
    #f1: sirimasen
    f1 = 2 * precision * recall / (precision + recall)

    d = {
            "accuracy" : accuracy,
            "precision" : precision,
            "recall": recall,
            "f1":f1
            }
    return d

if __name__ == "__main__":
    calc_score(sys.stdin,threshold=0.7)
