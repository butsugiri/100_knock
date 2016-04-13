# -*- coding: utf-8 -*-
"""
インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
"""
import sys

def main(fi):
    countries = {}
# 国名を読み込んで，辞書に保存
    with open("./data/country_name.txt","r") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.rstrip()
                if len(line.split()) > 1:
                    name = "_".join(line.split())
                    countries[line] = name

#行ごとに，国名辞書を走査して，国名の有無を判定
#国名が見つかったら，空白をアンダーバー_で置換
    for line in fi:
        line = line.rstrip()
        for country in countries.iterkeys():
            if country in line:
                line = line.replace(country,countries[country])
        print line

if __name__ == "__main__":
    main(sys.stdin)

"""
usage:
bzcat ./data/enwiki.txt.bz2 |  python q80.py | python q81.py
"""
