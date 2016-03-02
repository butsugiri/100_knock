# -*- coding: utf-8 -*-
"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""
import sys
from q30 import load_morph

def extract_longest_nouns(fi):
    queue = []
    for sent in load_morph(fi):
        for morph in sent:
            if morph["pos"] == u"名詞":
                queue.append(morph["sur"])
            else:
                if len(queue) > 1:
                    yield "".join(queue)
                queue = []

if __name__ == "__main__":
    for noun in extract_longest_nouns(sys.stdin):
        sys.stdout.write(noun + "\n")
