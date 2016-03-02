# -*- coding: utf-8 -*-
"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
"""
import sys
import re

def main(fi):
    p = re.compile(r"'+(?P<text>.*?)'+")
    for line in fi:
        line = line.rstrip()
        key = line.split("\t")[0]
        value = line.split("\t")[1]
        matchOB = p.finditer(value)
        if matchOB:
            for match in matchOB:
                value = match.group("text")
        print key + "\t" + value

if __name__ == "__main__":
    main(sys.stdin)

"""
❯ python q25.py < data/england.txt  | python q26.py
"""

