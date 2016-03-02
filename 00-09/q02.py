# -*- coding: utf-8 -*-
"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
import sys

def main():
    w1 = u"パトカー"
    w2 = u"タクシー"

    output = []
    for l1,l2 in zip(w1,w2):
        output.append(l1+l2)
    print "".join(output)

if __name__ == "__main__":
    main()
