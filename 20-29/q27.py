# -*- coding: utf-8 -*-
"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""
import sys
import re

def removebar(match):
    text = match.group(1)
    if "|" in text:
        return text.split("|")[-1]
    else:
        return text

def main(fi):
    p = re.compile(r"\[\[(?P<name>.*?)\]\]")
    for line in fi:
        line = line.rstrip()
        key, value = line.split("\t")
        subbed_value = p.sub(removebar,value)
        print key + "\t" + subbed_value

if __name__ == "__main__":
    main(sys.stdin)

"""
❯ python q25.py < data/england.txt  | python q26.py | python q27.py
BEFORE
国歌	[[女王陛下万歳|神よ女王陛下を守り給え]]
確立年月日1	[[927年]]／[[843年]]
確立年月日2	[[1707年]]
確立年月日3	[[1801年]]

AFTER
国歌	神よ女王陛下を守り給え
確立年月日1	927年／843年
確立年月日2	1707年
確立年月日3	1801年
"""
