# -*- coding: utf-8 -*-
"""
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．
"""
import sys

def main():
    print "EASY"

if __name__ == "__main__":
    main()
"""
db.artist.find({area:"Japan"}).count()
"""
