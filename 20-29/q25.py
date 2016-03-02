# -*- coding: utf-8 -*-
"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""
import sys
import re

def extract_BaseInfo(fi):
    isBaseInfo = False
    baseInfo = {}
    p = re.compile(r"^\|(?P<key>.+) = (?P<value>.+)")
    for line in fi:
        line = unicode(line.rstrip())
        if line.startswith(u"{{基礎情報"):
            isBaseInfo = True
        elif line == "}}":
            # sys.stderr.write("END of BaseInfo")
            isBaseInfo = False
            break
        elif isBaseInfo:
            matches = p.finditer(line)
            for match in matches:
                key = match.group("key")
                value = match.group("value")
                baseInfo[key] = value

    #辞書の中身を確認
    for k,v in baseInfo.iteritems():
        print "{}\t{}".format(k,v)

if __name__ == "__main__":
    extract_BaseInfo(sys.stdin)

"""
❯ python q25.py < data/england.txt
key:首相等氏名	value:デーヴィッド・キャメロン
key:首相等肩書	value:イギリスの首相|首相
key:人口順位	value:22
key:GDP/人	value:36,727<ref name="imf-statistics-gdp" />
key:人口統計年	value:2011
key:通貨	value:スターリング・ポンド|UKポンド]] (&pound;)
key:ISO 3166-1	value:GB / GBR
key:人口大きさ	value:1 E7
key:確立年月日4	value:1927年
key:国歌	value:女王陛下万歳|神よ女王陛下を守り給え
key:確立年月日1	value:927年]]／[[843年
key:確立年月日2	value:1707年
key:確立年月日3	value:1801年
"""
