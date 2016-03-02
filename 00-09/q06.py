# -*- coding: utf-8 -*-
"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
import sys

def ngram(n,string): #func from 005.py
    if len(string) >= n:
        ngram = [string[x:x+n] for x in range(len(string)-n+1)]
        return ngram

if __name__ == "__main__":
    text1 = "paraparaparadise"
    text2 = "paragraph"
    X = set(ngram(2,text1))
    Y = set(ngram(2,text2))
    print "和集合は:"
    print str(X.union(Y))
    print "積集合は:"
    print str(X.intersection(Y))
    print "差集合は:"
    print str(X.difference(Y))

    if "se" in X:
        print "se is in X"
    else:
        print "se is not in X"

    if "se" in Y:
        print "se is in X"
    else:
        print "se is not in X"
