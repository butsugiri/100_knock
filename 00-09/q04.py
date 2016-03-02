# -*- coding: utf-8 -*-
"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""
import sys

def normalize(text): #003.pyで使った関数と同様なので,importしてもよい.
    output = []
    for l in text:
        if l != "," and l != ".":
            output.append(l)
    return "".join(output)

def main(text): #textを受け取り，dict[str] = intの形で返す
    words = text.split(" ")
    atoms = {}
    for n, word in enumerate(words):
        if n+1 in [1,5,6,7,8,9,15,16,19]: #nは0から始まるため，+1が必要
            letter = word[0]
            atoms[letter] = n
        else:
            letters = word[0:2]
            atoms[letters] = n
    return atoms

if __name__ == "__main__":
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    text = normalize(text)
    print main(text)
