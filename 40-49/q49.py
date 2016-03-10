# -*- coding: utf-8 -*-
"""

"""
import sys
from q40 import Morph
from q41 import gen_chunks, Chunk
from itertools import combinations

# chunkと[chunk1,chunk2,...]が与えられたら
# chunkの係り先のchunkのindexをリストで返す関数
def follow_path(chunk,chunks):
    if chunk.dst:
        return [chunk.dst] + follow_path(chunks[chunk.dst],chunks)
    else:
        return []

# (follow_pathで)得たリストとchunksが与えられると，
# リストの中身に対応したchunkのリストを返す関数
def connect_path(path,chunks):
    output = []
    for n in path:
        output.append(chunks[n])
    return output

# chunkに含まれる最左の名詞を引数で置換する関数
def replace_leftmost_noun(chunk,x):
    new_chunk = Chunk() # 個人的ポイント 新しいインスタンスを作る
    new_chunk.dst = chunk.dst
    new_chunk.src = chunk.src
    noun_flag = False
    for morph in chunk.morphs:
        if morph.pos == u"名詞" and not noun_flag:
            # new_morphの中身は，surface以外は以前のものを流用する
            new_morph = Morph(x,morph.base,morph.pos,morph.pos1)
            new_chunk.morphs.append(new_morph)
            noun_flag = True
        else:
            new_chunk.morphs.append(morph)
    return new_chunk

def main(chunks):
#1. 名詞句を含む文節の集合を作る
    noun_chunks = []
    for n,chunk in enumerate(chunks):
        if chunk.contains(u"名詞"):
            noun_chunks.append((n,chunk))

#2. 文節集合から，chunk_iとchunk_jを選んでくる
    for i,j in combinations(noun_chunks,2):
        i_idx,chunk_i = i[0],i[1]
        j_idx,chunk_j = j[0],j[1]
        i_path = set(follow_path(chunk_i,chunks))
        i_path.add(i_idx)
        j_path = set(follow_path(chunk_j,chunks))
        j_path.add(j_idx)

        if i_path >= j_path:
#(3a)文節iからのpathが文節jからのpathを完全に包含している場合
            i2j_path = list(i_path - j_path)[1::]
            mid_term = connect_path(list(i2j_path),chunks)
            i_term = replace_leftmost_noun(chunk_i, u"X").chunk2str()
            j_term = replace_leftmost_noun(chunk_j, u"Y").chunk2str()
            mid = " -> ".join(x.chunk2str() for x in mid_term)
            if mid:
                output = [i_term,mid,j_term]
            else:
                output = [i_term,j_term]
            print " -> ".join(output)
        else:
#(3b)そうでない場合(途中で合流する場合)
            k_path = (i_path & j_path) #合流点以降のパス
            i_path = (i_path - k_path) #iからk(合流点)までのパス
            j_path = (j_path - k_path) #jからkまでのパス

            i_chunks = connect_path(sorted(list(i_path)),chunks)
            j_chunks = connect_path(sorted(list(j_path)),chunks)
            k_chunks = connect_path(sorted(list(k_path)),chunks)
            #chunkリストの先頭=名詞を含んだchunkであり，これをXとYで置換すればよい
            i_chunks[0] = replace_leftmost_noun(i_chunks[0],u"X")
            j_chunks[0] = replace_leftmost_noun(j_chunks[0],u"Y")

            #それぞれを->で結合しておく
            i_term = " -> ".join(x.chunk2str() for x in i_chunks)
            j_term = " -> ".join(x.chunk2str() for x in j_chunks)
            k_term = " -> ".join(x.chunk2str() for x in k_chunks)

            output = [i_term,j_term,k_term]
            print " | ".join(output)

if __name__ == "__main__":
    for chunks in gen_chunks(sys.stdin):
        main(chunks)
