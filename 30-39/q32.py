# -*- coding: utf-8 -*-
"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""
import sys
from q30 import load_morph

def extract_verb_base_form(fi):
    verb_base = set()
    for sent in load_morph(fi):
        for morph in sent:
            if morph["pos"] == u"動詞":
                verb_base.add(morph["base"])
    for sur in verb_base:
        print sur

if __name__ == "__main__":
    extract_verb_base_form(sys.stdin)

