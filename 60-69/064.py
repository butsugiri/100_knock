# -*- coding: utf-8 -*-
"""
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
"""
import sys,json,gzip
from pymongo import MongoClient

def main():
    mongo_client = MongoClient()
    db = mongo_client["artist"]
    with gzip.open("data/artist.json.gz","rb") as f:
        for line in f:
            artist = json.loads(line)
            db["artist"].insert(artist)
if __name__ == "__main__":
    main()

"""
インデックスはシェルからやりました
"""
