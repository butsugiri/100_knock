# -*- coding: utf-8 -*-
"""
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
"""
import sys

def calc_score(inp):
    tp = 0.0 # 正例と判定された正例
    tn = 0.0 # 負例と判定された負例
    fp = 0.0 # 正例と判定された負例
    fn = 0.0 # 負例と判定された正例

    for line in inp:
        line = line.strip()
        actual,label,_ = line.split("\t")
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
    #f1: ???
    f1 = 2 * precision * recall / (precision + recall)

    print "true positive:{} true negative:{}, false positive:{} false negative:{}".format(tp, tn, fp, fn)
    print "accuracy: {} ({}/{})".format(accuracy, tp+tn, tp+tn+fp+fn)
    print "precision: {} ({}/{})".format(precision, tp, tp+fp)
    print "recall: {} ({}/{})".format(recall, tp, tp+fn) 
    print "f1-score: {}".format(f1)


if __name__ == "__main__":
    calc_score(sys.stdin)
