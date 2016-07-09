# -*- coding: utf-8 -*-
"""
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．
"""
import sys
from q41 import gen_chunks
from collections import defaultdict

def extract_v_pattern(chunks):
    d = defaultdict(set)
    for chunk in chunks:
        if chunk.dst:
            dst = chunk.dst
            if chunks[dst].contains(u"動詞") and chunk.contains(u"助詞"):
                for morph in chunks[dst].morphs:
                    if morph.pos == u"動詞":
                        verb = morph.base
                for morph in chunk.morphs:
                    if morph.pos == u"助詞":
                        joshi = morph.surface
                d[verb].add(joshi)
    yield d
    d = defaultdict(set)

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        for d in extract_v_pattern(chunks):
            for verb, joshi in d.iteritems():
                joshi = " ".join(joshi)
                print "{}\t{}".format(verb,joshi)
