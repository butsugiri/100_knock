# -*- coding: utf-8 -*-
"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""
import sys
import random

def main(text):
    words = text.split(" ")
    output = []
    for word in words:
        if len(word) > 4:
            first = word[0]
            last = word[-1]
            middle = word[1:-1]
            lis = list(middle)
            random.shuffle(lis)
            middle = "".join(lis)
            word = first + middle + last
        output.append(word)
    return " ".join(output)


if __name__ == "__main__":
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    text2 = "My understanding of the universe has been completely altered"
    print main(text)
    print main(text2)
