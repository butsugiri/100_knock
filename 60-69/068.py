# -*- coding: utf-8 -*-
"""
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
"""
import sys
from pymongo import MongoClient
from pymongo import DESCENDING

def main():
    mongo_client = MongoClient()
    db = mongo_client["artist"]
    cursor = db["artist"].find({"tags.value":"dance", "rating.count":{"$exists":True}})
    for document in cursor.sort("rating.count",DESCENDING):
        artist_name = document["name"]
        count = document["rating"]["count"]
        print artist_name + "\t" + "count: " + str(count)

if __name__ == "__main__":
    main()

"""
実行例
python 068.py

出力結果
Madonna count: 26
Björk   count: 23
The Prodigy     count: 23
Rihanna count: 15
Britney Spears  count: 13
Maroon 5        count: 11
Adam Lambert    count: 7
Fatboy Slim     count: 7
Basement Jaxx   count: 6
Cornershop      count: 5
Gigi D’Agostino count: 5
Duran Duran     count: 5
Deborah Harry   count: 4
Erasure count: 4
Bananarama      count: 4
Ke$ha   count: 4
The Faint       count: 4
Cher    count: 4
Chris Brown     count: 4
Apollo 440      count: 3
Pnau    count: 3
Soulwax count: 3
LMFAO   count: 3
"""
