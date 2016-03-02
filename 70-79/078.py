# -*- coding: utf-8 -*-
"""
78. 5分割交差検定
5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．

5分割交差検定 by classias
classias-train --type=binary --algorithm=lbfgs.logistic --cross-validate --split=5 baseline.txt > baseline.log

baseline.logを読み込んで作業

実行例
python 078.py < baseline.log
"""
import sys
import numpy as np
from collections import deque

def main(log_file):
    buff = deque(maxlen=2)
    a = []
    p = []
    r = []
    f = []
    for line in log_file:
        line = line.strip()
        if "terminated" in line:
            accuracy = float(buff[0].split(" ")[1])
            precision = float(buff[1].split(" ")[4])
            recall = float(buff[1].split(" ")[6])
            f1 = float(buff[1].split(" ")[8])
            a.append(accuracy)
            p.append(precision)
            r.append(recall)
            f.append(f1)
        elif line:
            buff.append(line)
    accuracy_mean = np.array(a,dtype=np.float).mean()
    precision_mean = np.array(p,dtype=np.float).mean()
    recall_mean = np.array(r,dtype=np.float).mean()
    f1_mean = np.array(f,dtype=np.float).mean()

    n = len(a)
    print "The result of {}-fold cross validation:".format(n)
    print "Accuracy mean is {}".format(accuracy_mean)
    print "Precision mean is {}".format(precision_mean)
    print "Recall mean is {}".format(recall_mean)
    print "f1 mean is {}".format(f1_mean)

if __name__ == "__main__":
    main(sys.stdin)

"""
解説
***** Iteration #113 *****
Loss: 3209.07
Feature L2-norm: 27.538
Error norm: 2.23117
Active features: 13176 / 14632
Line search trials: 1
Line search step: 1
Seconds required for this iteration: 0.001703
Accuracy: 0.7482 (1596/2133) 💩💩💩ここを読む!
Micro P, R, F1: 0.7479 (795/1063), 0.7472 (795/1064), 0.7475 💩💩💩ここを読む!

L-BFGS terminated with the stopping criteria
Seconds required: 0.217275
===== Cross validation (2/5) =====
terminatedの行を探して，そのすぐ上を読めば良い
(それがn回目の交差検定の結果)
"""
