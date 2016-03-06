# -*- coding: utf-8 -*-
"""
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ.
"""
import sys
from q41 import gen_chunks

def follow_paths(chunks):
    phrase = []
    for chunk in chunks:
        if chunk.contains(u"名詞"):
            phrase.append(chunk.chunk2str())
            dst = chunk.dst
            while dst:
                phrase.append(chunks[dst].chunk2str())
                dst = chunks[dst].dst
            if len(phrase) > 1:
                yield " -> ".join(phrase)
            phrase = []

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        for path in follow_paths(chunks):
            sys.stdout.write(path+"\n")
        print
