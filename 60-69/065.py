# -*- coding: utf-8 -*-
"""
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．さらに，これと同様の処理を行うプログラムを実装せよ．
"""
import sys
from pymongo import MongoClient

def main():
    mongo_client = MongoClient()
    db = mongo_client["artist"]
    data = db["artist"].find_one({"name":"Queen", "area":"United Kingdom"})
    if data:
        band_name = data["name"]
        area = data["area"]
        tags = ",".join([x["value"] for x in data["tags"]])
        print "バンド名: " + band_name + "\t" + "活動国: " + area
        print "関連する単語: " + tags

if __name__ == "__main__":
    main()

"""
シェルから
db.artist.find({name:Queen})
でいけるっしょ
"""

