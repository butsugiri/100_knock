# -*- coding: utf-8 -*-
"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""
import sys
from q30 import load_morph

def extract_verb_surface(fi):
    verb_surface = set()
    for sent in load_morph(fi):
        for morph in sent:
            if morph["pos"] == u"動詞":
                verb_surface.add(morph["sur"])
    for sur in verb_surface:
        print sur

if __name__ == "__main__":
    extract_verb_surface(sys.stdin)
