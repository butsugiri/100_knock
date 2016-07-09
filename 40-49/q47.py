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
            if len(chunk.morphs) == 2 \
                    and chunk.morphs[0].pos1 == u"サ変接続" \
                    and chunk.morphs[1].surface == u"を":
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
            for morph in chunk.morphs:
                if morph.pos == u"助詞":
                    joshi = morph.surface
            joshi_lis.append(joshi) #最右の助詞だけとなる
            phrase_lis.append(chunk.chunk2str())
        if joshi_lis and phrase_lis:
            joshi = " ".join(joshi_lis)
            phrase = " ".join(phrase_lis)
            print "{}\t{}\t{}".format(k,joshi,phrase)

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        extract_sahen(chunks)

"""
output

決心をする      と      こうと
返報をする      んで    偸んで
昼寝をする      が      彼が
迫害を加える    て      追い廻して
投書をする      て へ   やって ほととぎすへ
話をする        に      時に
昼寝をする      て      出て
欠伸をする      から て て      なったから して 押し出して
報道をする      に      耳に
御馳走を食う    と      見ると
雑談をする      は ながら       黒は 寝転びながら
思案を定める    は と   吾輩は 若くはないと
呼吸を飲み込む  から    なってから
御馳走をあるく  て って なって 猟って
放蕩をする      が も   ものだからが 云うよりも
写生を力む      に従って        忠告に従って
写生をする      から    しから
対話を聞く      で      椽側で
苦心をする      から    さっきから
"""
