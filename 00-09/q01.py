# -*- coding: utf-8 -*-
"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""
import sys

def main():
    text = u"パタトカクシーー"
    print "".join([x for n,x in enumerate(text) if n % 2 == 0]) #リスト内包表記
    print text[0] + text[2] + text[4] + text[6] #ナイーブにやる場合

    # リスト内包表記を使わない場合
    output = []
    for n,x in enumerate(text):
        if n % 2 == 0:
            output.append(x)
    print "".join(output)

if __name__ == "__main__":
    main()
