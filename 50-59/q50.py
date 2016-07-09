# -*- coding: utf-8 -*-
"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

実行例
python q50.py < ./data/nlp.txt
"""
import sys
import re

fi = sys.stdin
fo = sys.stdout

def split_line(match):
    return match.group().replace(" ","\n")

p = re.compile(r"[.;:?!]\s[A-Z]")

for line in fi:
    fo.write(p.sub(split_line,line))

