# -*- coding: utf-8 -*-
"""
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
"""
import sys

def return_stop_words(input):
    stop_words = set()
    for line in input:
        line = line.rstrip()
        stop_words.add(line)
    return stop_words

def is_stop_word(word,stop_words):
    if word in stop_words:
        return True
    else:
        return False

if __name__ == "__main__":
    stop_words = return_stop_words(sys.stdin)
    print is_stop_word("hogehogehoge", stop_words)
    print is_stop_word("a", stop_words)
