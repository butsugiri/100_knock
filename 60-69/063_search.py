# -*- coding: utf-8 -*-
"""
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
"""

import sys,plyvel,json,gzip,pickle,argparse

def main(args):
    name = args.name
    artist_db = plyvel.DB("./DB/tag.ldb",create_if_missing=True)
    tag_serialized = artist_db.get(name)
    tag_info = pickle.loads(tag_serialized)
    print "About: " + name
    for tag in tag_info:
        count = tag["count"]
        value = tag["value"]
        print "count: " + str(count) + "\t" + "value: " + value
    artist_db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Tag Database")
    parser.add_argument('-n', '--name', dest='name', default="", type=str,help='name of the artist')
    args = parser.parse_args()
    main(args)

"""
$ python 063_search.py -n Oasis
About: Oasis
count: 1	value: rock
count: 3	value: britpop
count: 4	value: british
count: 1	value: uk
count: 1	value: britannique
count: 1	value: rock and indie
count: 1	value: england
count: 1	value: manchester
"""

