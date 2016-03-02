# -*- coding: utf-8 -*-
"""
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
"""
import sys
from itertools import combinations
from collections import defaultdict

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self,dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []
        self.n = 0 #自分で勝手に作った．文中のn番目の文節ということを示す．

    def contains(self,pos):
        pos_list = [morph.pos for morph in self.morphs]
        if pos in pos_list:
            return True
        else:
            return False

def return_single_sent():
    sent = []
    for line in sys.stdin:
        line = line.rstrip()
        sent.append(line)
        if line == "EOS":
            yield sent
            sent = []
            continue

def parse_CaboCha_output(inp):
    chunks = []
    new_chunk = None
    for sent in inp:
        for line in sent:
            line = line.rstrip()
            if line.startswith("*"):
                if new_chunk:
                    chunks.append(new_chunk)
                dst = line.split(" ")[2].split("D")[0]
                if dst == "-1":
                    new_chunk = Chunk(None)
                else:
                    new_chunk = Chunk(int(dst))
            elif line =="EOS":
                if new_chunk:
                    chunks.append(new_chunk)
                yield read_kakari_sources(chunks)
                chunks = []
                new_chunk = None
                continue
            else:
                surface, detail = line.split("\t")
                base = detail.split(",")[6]
                pos = detail.split(",")[0]
                pos1 = detail.split(",")[1]
                if pos != "記号": #問題文いわく，記号は含めないこと．
                    new_chunk.morphs.append(Morph(surface,base,pos,pos1))

def read_kakari_sources(chunks): #Chunks[chunks,chunks,...]に係り元の情報を付加する関数
    for n,chunk in enumerate(chunks):
        if chunk.dst:
            dst = chunk.dst
            chunks[dst].srcs.append(n)
    return chunks

def extract_kakari_paths_from_noun(chunks):
    phrase_with_nouns = []
    #再帰的にパスを辿る関数 辿れなくなったらおわり
    def return_path(chunk,chunks):
        if chunk.dst:
            return [chunk.dst] + return_path(chunks[chunk.dst],chunks)
        else:
            return []

    #connect_path: 係り受けのpath=[1,2,5,...]に対応するchunkを[chunk]として返す
    def connect_path(chunks, path):
        connected_chunks = []
        for n,chunk in enumerate(chunks):
            if n in path:
                connected_chunks.append(chunk)
        return connected_chunks

    #[chunk]の中から，["Yで","始めて","人間という","ものを"]みたいなのを返す
    def connect_chunks(chunks):
        str_seq = []
        for chunk in chunks:
            output = "".join([x.surface for x in chunk.morphs])
            str_seq.append(output)
        return str_seq

    def replace_leftmost_noun(replace, chunks):
        for chunk in chunks:
            for morph in chunk.morphs:
                if morph.pos == "名詞":
                    morph.surface = replace
                    break
            break
        return chunks

    #まず，名詞句を含む文節のchunkを抽出し，[chunk]を作る
    for n,chunk in enumerate(chunks):
        if chunk.contains("名詞"):
            chunk.n = n
            phrase_with_nouns.append(chunk)

    #名詞句を含む文節を二つずつ選んで
    for chunk_i, chunk_j in combinations(phrase_with_nouns,2):
        i_str_list = []
        j_str_list = []
        i_path = sorted([chunk_i.n] + return_path(chunk_i,chunks))
        j_path = sorted([chunk_j.n] + return_path(chunk_j,chunks))
        i_path_set = set(i_path)
        j_path_set = set(j_path)
        set_length = min([len(i_path_set),len(j_path_set)])
        #1. 文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合
        if len(i_path_set.intersection(j_path_set)) < set_length:
            k_path = i_path[len(i_path_set.intersection(j_path_set))*(-1)::]
            i_path = i_path[0:len(i_path_set.intersection(j_path_set))*(-1)]
            j_path = j_path[0:len(i_path_set.intersection(j_path_set))*(-1)]
            i_chunks = replace_leftmost_noun("X",connect_path(chunks, i_path))
            j_chunks = replace_leftmost_noun("Y",connect_path(chunks, j_path))
            k_chunks = connect_path(chunks,k_path)
            output = [" -> ".join(connect_chunks(i_chunks))," -> ".join(connect_chunks(j_chunks))," -> ".join(connect_chunks(k_chunks))]
            print " | ".join(output)
        #2. 文節iから構文木の根に至る経路上に文節jが存在する場合
        else:
            i_path = list(i_path_set.symmetric_difference(j_path_set))
            if len(i_path_set) > len(j_path_set):
                j_path = [j_path[0]]
            else:
                j_path = [i_path[0]]
            i_chunks = replace_leftmost_noun("X",connect_path(chunks, i_path))
            j_chunks = replace_leftmost_noun("Y",connect_path(chunks, j_path))
            output = [" -> ".join(connect_chunks(i_chunks))," -> ".join(connect_chunks(j_chunks))]
            print " -> ".join(output)


if __name__ == "__main__":
    for chunks in parse_CaboCha_output(return_single_sent()):
        extract_kakari_paths_from_noun(chunks)

"""
input
head -100 data/neko.txt.cabocha | python 049.py
output
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Yという
Xで -> 始めて -> Yという -> Yを
Xという -> Yを

なんかYの後に助詞が出てくる…
"""

