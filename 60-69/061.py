# -*- coding: utf-8 -*-
"""
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
"""

"""
python 061.py -n Oasis
Oasis is from United import Kingdom
Yeah
"""
import sys
import plyvel
import argparse

def main(db_source,args):
    name = args.name
    artist_db = plyvel.DB(db_source)
    if artist_db.get(name):
        area = artist_db.get(name)
    else:
        exit(1)
    artist_db.close()
    print name + " is from " + area

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument('-n', '--name', dest='name', default="", type=str,help='name of the artist that you wanna know about')
    args = parser.parse_args()
    main("./DB/artist.ldb",args)
