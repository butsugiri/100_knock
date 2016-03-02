# -*- coding: utf-8 -*-
"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""
import sys
from lxml import etree

def main():
    person_name = []
    tree = etree.parse("./data/nlp.xml")
    token = tree.xpath("/root/document/sentences/sentence/tokens/token")
    for element in token:
        if element.find("NER").text == "PERSON":
            person_name.append(element[0].text) #token直下にwordタグがあると仮定している
        else:
            if person_name:
                print " ".join(person_name)
                person_name = []

if __name__ == "__main__":
    main()

"""
output
Alan Turing
ELIZA
Joseph Weizenbaum
Wilensky
Meehan
Lehnert
Carbonell
Lehnert
Jabberwacky
Moore
"""
