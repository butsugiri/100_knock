# -*- coding: utf-8 -*-
"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""
import sys
from q41 import gen_chunks

def extract_noun2verb(chunks):
    for chunk in chunks:
        if chunk.dst:
            dst = chunk.dst
            if chunks[dst].contains(u"動詞") and chunk.contains(u"名詞"):
                dst_txt = chunks[dst].chunk2str()
                src_txt = chunk.chunk2str()
                yield "{}\t{}".format(src_txt,dst_txt)

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        for sent in extract_noun2verb(chunks):
            print sent
