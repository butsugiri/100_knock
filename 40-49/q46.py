# -*- coding: utf-8 -*-
"""
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

実行例
python q46.py < ./data/neko.txt.cabocha
"""
import sys
from q41 import gen_chunks
from collections import defaultdict

def extract_verb_frame(chunks):
    d = defaultdict(list)
    #key:動詞 value = [助詞を含んだchunk,.....]となるdを用意
    for chunk in chunks:
        if chunk.dst:
            dst = chunk.dst
            if chunks[dst].contains(u"動詞") and chunk.contains(u"助詞"):
                for morph in chunks[dst].morphs:
                    if morph.pos == u"動詞":
                        verb = morph.base
                        d[verb].append(chunk)

    #出力のためにdの中身をいじる
    #chunkを取り出して，助詞部分 + 文節全体を抽出
    #それぞれをリストにappendして，最後にjoin
    #i.e. joshi_lis = [は，を，が] phrase_lis = [本当は,君を,りんごが]
    for k,v in d.iteritems():
        joshi_lis = []
        phrase_lis = []
        for chunk in v:
            for morph in chunk.morphs:
                if morph.pos == u"助詞":
                    joshi = morph.surface
            joshi_lis.append(joshi)
            phrase_lis.append(chunk.chunk2str())
        if joshi_lis and phrase_lis:
            joshi = " ".join(joshi_lis)
            phrase = " ".join(phrase_lis)
            print "{}\t{}\t{}".format(k,joshi,phrase)

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        extract_verb_frame(chunks)

"""
output

つく    か が   生れたか 見当が
生れる  で      どこで
する    て は   泣いて いた事だけは
泣く    で      所で
いる    て は   泣いて いた事だけは
見る    は を   吾輩は ものを
始める  で      ここで
聞く    で      あとで
食う    て      煮て
煮る    て      捕えて
捕える  を      我々を
思う    から    なかったから
載せる  に      掌に
持ち上げる      て と   載せられて スーと
られる  に て と        掌に 載せられて スーと
ある    が      感じが
見る    て を の        落ちついて 顔を ものの
落ちつく        で      上で
残る    が でも 感じが 今でも
思う    と      ものだと
"""
