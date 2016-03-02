# -*- coding: utf-8 -*-
"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

gzcat data/jawiki-country.json.gz | python q20.py > ./data/england.txt
england.txtに本文を保存した
"""
import sys
import json
from pprint import pprint

def main(fi):
    for line in fi:
        line = line.rstrip()
        article = json.loads(line)
        if article["title"] == u"イギリス":
            print article["text"]

if __name__ == "__main__":
    main(sys.stdin)
