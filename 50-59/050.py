# -*- coding: utf-8 -*-
"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
"""
import sys
import re

def main():
    pattern = r"([.:;?!]) ([A-Z])"
    repatter = re.compile(pattern)
    for line in sys.stdin:
        line = re.sub(repatter,r"\1\n\2",line.rstrip())
        print line

if __name__ == "__main__":
    main()
