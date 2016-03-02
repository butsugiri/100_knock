# -*- coding: utf-8 -*-
"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""
import sys
import re
from q27 import removebar

def main(fi):
    xml_p = re.compile(r"<.+>")
    link_p = re.compile(r"{{(.+)}}")
    for line in fi:
        line = line.rstrip()
        key, value = line.split("\t")
        value = xml_p.sub("",value)
        value = link_p.sub(removebar,value)
        if value and key:
            print key + "\t" + value

if __name__ == "__main__":
    main(sys.stdin)

"""
❯ python q25.py < data/england.txt  | python q26.py | python q27.py | python q28.py
<ref name="imf-statistics-gdp" />のようなXML的マークアップと，
{{lang|fr|Dieu et mon droit}}のようなリンクを削除
前者についてはタグごと削除
後者については{{fuga|haga|hoge}}のhogeのみ抽出
"""

