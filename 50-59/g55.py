# -*- coding: utf-8 -*-
"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．

"""
import sys
from lxml import etree
from itertools import groupby

def yield_names(tree):
    tokens = tree.xpath("//token")
    for is_name, token in groupby(tokens, key=lambda x:x.find("NER").text == "PERSON"):
        if is_name:
            # word is the first element of each token
            yield " ".join(x[0].text for x in token)

if __name__ == "__main__":
    with open("./data/out.xml", "r") as fi:
        tree = etree.parse(fi)
        print type(tree)
        for name in yield_names(tree):
            print name

"""
~/Dropbox/lab/prog/100_knock/50-59 master* 38s
❯ python g55.py
Alan Turing
Joseph Weizenbaum
MARGIE
Schank
Wilensky
Meehan
Lehnert
Carbonell
Lehnert
Jabberwacky
Moore
"""
