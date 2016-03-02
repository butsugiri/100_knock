# -*- coding: utf-8 -*-
"""
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ．
"""
import sys
from pymongo import MongoClient

def main():
    mongo_client = MongoClient()
    db = mongo_client["artist"]
    cursor = db["artist"].find({"aliases.name":{"$exists":True}})
    for document in cursor:
        artist_name = document["name"]
        alias_name = ",".join([x["name"] for x in document["aliases"]])
        print artist_name + " is also known as: "
        print alias_name + "\n"

if __name__ == "__main__":
    main()

"""
python 067.py
"""
