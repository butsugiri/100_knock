# -*- coding: utf-8 -*-
"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""
import sys

def cipher(text):
    output = []
    for x in text:
        if x.islower():
            x = chr(219 - ord(x))
        else:
            pass
        output.append(x)

    return "".join(output)

if __name__ == "__main__":
    text = "Jump in the pool played by Friendly Fires"
    encrypted_text = cipher(text)
    decrypted_text = cipher(encrypted_text)

    print "Original Text is " + text
    print "Encrypted Text is " + encrypted_text
    print "Decrypted Text is " + decrypted_text
