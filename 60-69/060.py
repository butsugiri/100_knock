# -*- coding: utf-8 -*-
"""
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
"""
import sys
import plyvel
import json
import gzip


def main():
    with gzip.open("data/artist.json.gz","rb") as f:
        for line in f:
            artist = json.loads(line)
            if "area" in artist:
                key = artist["name"].encode('utf-8')
                value = artist["area"].encode('utf-8')
                artist_db.put(key,value)

if __name__ == "__main__":
    artist_db = plyvel.DB("./DB/artist.ldb",create_if_missing=True) #なければ作る
    main()
    artist_db.close()
