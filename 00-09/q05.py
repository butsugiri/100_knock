# -*- coding: utf-8 -*-
"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""
import sys

def ngram1(n,string): #for文ver.
    n_gram = []
    if len(string) >= n:
        for x in range(0, len(string)-n+1):
            n_gram.append(string[x:x+n])
        return n_gram

def ngram2(n,string): #内包表記ver.
    if len(string) >= n:
        ngram = [string[x:x+n] for x in range(len(string)-n+1)]
        return ngram

if __name__ == "__main__":
    print ngram1(2, "I am an NLPer".split(" ")) #単語bi-gram
    print ngram2(2, "I am an NLPer") #文字bi-gram
    
