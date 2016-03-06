# -*- coding: utf-8 -*-
"""
"""
import sys
from q41 import gen_chunks
from collections import defaultdict

def extract_sahen(chunks):
    d = defaultdict(list)
    #key:動詞 value = [助詞を含んだchunk,.....]となるdを用意
    for n,chunk in enumerate(chunks):
        if chunk.dst:
            dst = chunk.dst
            if len(chunk.morphs) == 2 and chunk.morphs[0].pos1 == u"サ変接続" and chunk.morphs[1].surface == u"を":
                if chunks[dst].contains(u"動詞"):
                    for morph in chunks[dst].morphs:
                        if morph.pos == u"動詞":
                            verb = morph.base
                            phrase = chunk.chunk2str() + verb
                            break #最左の動詞だけほしいので
                    for src in chunks[dst].src:
                        if chunks[src].contains(u"助詞") and src != n:
                            d[phrase].append(chunks[src])

    for k,v in d.iteritems():
        joshi_lis = []
        phrase_lis = []
        for chunk in v:
            temp = [] 
#tempは，一つの文節の中に複数の助詞が含まれている場合に必要
# 「及ばんさと」中には「さ」「と」が助詞として含まれているので，そのまま出力すると両方出てしまう
# 本当はq46も直すべき
            for morph in chunk.morphs:
                if morph.pos == u"助詞":
                    temp.append(morph.surface)
            joshi_lis.append(temp[-1]) #上記の理由にて，最右の助詞だけを抽出
            phrase_lis.append(chunk.chunk2str())
        if joshi_lis and phrase_lis:
            joshi = " ".join(joshi_lis)
            phrase = " ".join(phrase_lis)
            print "{}\t{}\t{}".format(k,joshi,phrase)

def format_chunks(chunks):
    pass
if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        extract_sahen(chunks)

