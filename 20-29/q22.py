# -*- coding: utf-8 -*-
"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ
"""
import sys
import re

def main(fi):
    p = re.compile(r"^\[\[Category:(?P<category>.+)\]\]$")
    for line in fi:
        line = line.rstrip()
        matchOB = p.match(line)
        if matchOB:
            print matchOB.group("category").rstrip("|*")

if __name__ == "__main__":
    main(sys.stdin)

"""
❯ python q21.py < data/england.txt | python q22.py
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国|くれいとふりてん
1801年に設立された州・地域
"""
