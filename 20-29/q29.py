# -*- coding: utf-8 -*-
"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
"""
import sys
import urllib
import json

def main(fi):
    #標準入力をなめて，基礎情報の辞書を作る
    baseInfo = {}
    for line in fi:
        line = line.rstrip()
        key,value = line.split("\t")
        baseInfo[unicode(key)] = unicode(value)

    #辞書から国旗画像のファイル名を取得
    filename = "File:" + baseInfo[u"国旗画像"]
    query = {
            "action":"query",
            "format":"json",
            "prop":"imageinfo",
            "titles":filename,
            "iiprop":"url"
            }
    #urlencodeを使うとmap型をいい感じに展開できる
    params = urllib.urlencode(query)
    api_endpoint = "http://ja.wikipedia.org/w/api.php?"
    url = urllib.urlopen(api_endpoint + params)
    response = json.load(url)
    print response["query"]["pages"]["-1"]["imageinfo"][0]["url"]

if __name__ == "__main__":
    main(sys.stdin)

"""
実行例
❯ python q25.py < data/england.txt  | python q26.py | python q27.py | python q28.py | python q29.py
"""
