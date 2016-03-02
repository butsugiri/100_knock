# -*- coding: utf-8 -*-
"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""
import sys
from q30 import load_morph

def extract_sahen_noun(fi):
    sahen_noun = set()
    for sent in load_morph(fi):
        for morph in sent:
            if morph["pos"] == u"名詞" and morph["pos1"] == u"サ変接続":
                sahen_noun.add(morph["sur"])
    for sur in sahen_noun:
        print sur

if __name__ == "__main__":
    extract_sahen_noun(sys.stdin)

