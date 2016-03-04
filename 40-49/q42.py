# -*- coding: utf-8 -*-
"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""
import sys
from q41 import gen_chunks

def extract_src_dst(chunks):
    for chunk in chunks:
        if chunk.dst:
            dst = chunk.dst
            dst_txt = chunks[dst].chunk2str()
            src_txt = chunk.chunk2str()
            yield "{}\t{}".format(src_txt,dst_txt)

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        for sent in extract_src_dst(chunks):
            print sent
