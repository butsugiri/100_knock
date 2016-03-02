# -*- coding: utf-8 -*-
"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""
import sys
from q30 import load_morph

def consecutive_nouns(fi):
    is_prev_noun = False
    # queueに「noun+の+noun」を積んでいく
    queue = []
    connected_nouns = set()
    for sent in load_morph(fi):
        for morph in sent:
            if morph["pos"] == u"名詞" and not queue:
                is_prev_noun = True
                queue.append(morph["sur"])
            elif is_prev_noun and morph["sur"] == u"の":
                queue.append(u"の")
            elif len(queue) > 1 and morph["pos"] == u"名詞":
                queue.append(morph["sur"])
                connected_nouns.add("".join(queue))
                queue = []
                is_prev_noun = False
            else:
                # うまくいかなかったらqueueを空にして最初から
                queue = []
                is_prev_noun = False
    return connected_nouns

if __name__ == "__main__":
    nouns = consecutive_nouns(sys.stdin)
    for noun in list(nouns):
        print noun

