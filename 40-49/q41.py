# -*- coding: utf-8 -*-
"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．

実行例:
cat data/neko.txt.cabocha | awk "NR==1,NR==43" | python q41.py
awk "NR==hogehoeg"の書き方で，指定した行を抽出できる．
コンマで繋げばその範囲の行を抽出できる．
セミコロン(;)ならば指定した行のみ抽出できる．
"""
import sys
from q40 import Morph

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.src = []

    #chunkに含まれるテキスト(記号以外)を返すクラスメソッド
    #q42で初登場
    def chunk2str(self):
        output = []
        for morph in self.morphs:
            if morph.pos == u"記号":
                pass
            else:
                output.append(morph.surface)
        return "".join(output)

    #文節にある品詞が含まれているか否かを返す
    #q43で初登場
    def contains(self,pos):
        pos = unicode(pos)
        pos_list = [x.pos for x in self.morphs]
        return pos in pos_list

    def __repr__(self):
        return " ".join(x.surface for x in self.morphs)

def gen_chunks(fi):
    def follow_srcs(chunks):
        for n,chunk in enumerate(chunks):
            if chunk.dst:
                dst = chunk.dst
                chunks[dst].src.append(n)
        return chunks

    chunk = None
    chunks = []
    for line in fi:
        line = line.rstrip()
        if line.startswith("*"):
            if chunk:
                chunks.append(chunk)
            chunk = Chunk()
            dst = int(line.split()[2].rstrip("D"))
            if dst != -1:
                chunk.dst = dst
        elif line == "EOS":
            if chunks:
                chunks.append(chunk)
                yield follow_srcs(chunks)
            chunk = None
            chunks = []
            continue
        else:
            sur = unicode(line.split("\t")[0])
            detail = line.split("\t")[1].split(",")
            base = unicode(detail[6])
            pos = unicode(detail[0])
            pos1 = unicode(detail[1])
            chunk.morphs.append(Morph(sur,base,pos,pos1))

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        for n, chunk in enumerate(chunks):
            print "{}番目の文節:".format(n)
            print "係り先: {}".format(chunk.dst)
            print "係り元: {}".format(chunk.src)
            print "内容: {}\n".format(" ".join(x.surface for x in chunk.morphs))
