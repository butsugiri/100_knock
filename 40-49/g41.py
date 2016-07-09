# -*- coding: utf-8 -*-
"""
41をgroupbyで(ry
"""
import sys
from itertools import groupby
from g40 import classify_cabocha_line, Line, Morph

class Chunk(object):
    def __init__(self,info,morphs):
        info = info.rstrip()
        self.idx = int(info.split()[1])
        self.dst = int(info.split()[2].rstrip("D"))
        self.morphs = morphs
        self.srcs = []

    def __str__(self):
        return " ".join(morph.sur for morph in self.morphs)

class Sentence(object):
    def __init__(self, chunks):
#chunksを読んで係り先の情報を付与する
        for chunk in chunks:
            if chunk.dst > 0:
                chunks[chunk.dst].srcs.append(chunk.idx)
        self.chunks = chunks

def parse_cabocha(fi):
    for is_eos, sections in groupby(fi, key=lambda l:l=="EOS\n"):
        out = []
        if not is_eos:
            for _type, section in groupby(sections, key=classify_cabocha_line):
                if _type == Line.CHUNK:
                    chunk_info = next(section)
                elif _type == Line.MORPH:
                    out.append(Chunk(chunk_info, [Morph(line) for line in section]))
            yield Sentence(out)

if __name__ == "__main__":
    for sent in parse_cabocha(sys.stdin):
        for chunk in sent.chunks:
            print "#{}: {}\t kakari from {}".format(chunk.idx,str(chunk),chunk.srcs)
