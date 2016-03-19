# -*- coding: utf-8 -*-
"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""
import sys
from lxml import etree

def yield_names(fi):
    tokens = fi.xpath("//token")
    is_prev_name = False
    queue = []
    for token in tokens:
        for elem in token.iter("NER"):
            if elem.text == "PERSON":
                queue.append(token[0].text)
                is_prev_name = True
            elif is_prev_name:
                is_prev_name = False
                yield " ".join(queue)
                queue = []


if __name__ == "__main__":
    with open("./data/out.xml","r") as fi:
        tree = etree.parse(fi)
        for name in yield_names(tree):
            print name

