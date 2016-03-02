# -*- coding: utf-8 -*-
"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""
import sys
import plyvel

def main(db_source):
    n = 0
    artist_db = plyvel.DB(db_source)
    for name,area in artist_db:
        if area == "Japan":
            n += 1
    artist_db.close()
    print "日本のアーティストは合計" + str(n) + "人"

if __name__ == "__main__":
    main("./DB/artist.ldb")
