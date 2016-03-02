# -*- coding: utf-8 -*-
"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""
import sys
import re

def main(fi):
    p = re.compile(r"^\[\[Category:.*\]\]$")
    for line in fi:
        line = unicode(line.rstrip())
        if p.match(line):
            print line

if __name__ == "__main__":
    main(sys.stdin)

"""
❯ python q21.py < data/england.txt
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""
