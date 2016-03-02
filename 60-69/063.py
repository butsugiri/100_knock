# -*- coding: utf-8 -*-
"""
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
"""
import sys
import plyvel
import json
import gzip
import pickle

def main():
    artist_db = plyvel.DB("./DB/tag.ldb",create_if_missing=True) #なければ作る
    artist_tag = []
    with gzip.open("data/artist.json.gz","rb") as f:
        for line in f:
            artist = json.loads(line)
            if "tags" in artist:
                name = artist["name"].encode('utf-8')
                for tag in artist["tags"]:
                    artist_tag.append(tag)
                artist_db.put(name,pickle.dumps(artist_tag))
                artist_tag = []
    artist_db.close()

if __name__ == "__main__":
    main()

