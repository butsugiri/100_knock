# -*- coding: utf-8 -*-
"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""
import sys
import re

def main(fi):
    p = re.compile(r"^(?P<level>=+)(?P<section_name>.+?)=+$")
    for line in fi:
        line = line.rstrip()
        matchOB = p.match(line)
        if matchOB:
            section_name = matchOB.group("section_name")
            level = len(matchOB.group("level")) - 1 # 問いわく，==hoge==でレベル1なので
            print "{}\tレベル{}".format(section_name,level)

if __name__ == "__main__":
    main(sys.stdin)

"""
❯ python q23.py < data/england.txt
国名	レベル1
歴史	レベル1
地理	レベル1
気候	レベル2
政治	レベル1
外交と軍事	レベル1
地方行政区分	レベル1
主要都市	レベル2
科学技術	レベル1
経済	レベル1
鉱業	レベル2
農業	レベル2
貿易	レベル2
"""
