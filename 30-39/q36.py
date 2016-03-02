# -*- coding: utf-8 -*-
"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""
import sys
from q30 import load_morph
from collections import defaultdict

def count_terms(fi):
    d = defaultdict(int)
    for sent in load_morph(fi):
        for morph in sent:
            d[morph["base"]] += 1
    return d

if __name__ == "__main__":
    terms = count_terms(sys.stdin)
    for k,v in sorted(terms.items(),key=lambda x:x[1], reverse=True):
        print "{}\t{}".format(k,v)
