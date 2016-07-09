# -*- coding: utf-8 -*-
"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ
"""
import sys
from lxml import etree
from collections import defaultdict

def replace_mention(tree):
    corefs = tree.xpath("//coreference/coreference")
    coref_dict = defaultdict(lambda: defaultdict())
    for coref in corefs:
        mentions = coref.xpath(".//mention")
        for mention in mentions:
            if mention.attrib.get("representative") == "true":
                rep = mention.find("text").text
            else:
                s_id = int(mention.find("sentence").text)
                start = int(mention.find("start").text)
                end = int(mention.find("end").text)
                coref_dict[s_id][start] = (rep,end)
    return coref_dict

def replace_by_coreference(tree,coref):
    for sent in tree.xpath("//sentence[@id]"):
        endpoint = -1
        s_id = int(sent.attrib.get("id"))
        for token in sent.iter("token"):
            w_idx = int(token.attrib.get("id"))
            if w_idx in coref[s_id]:
                print coref[s_id][w_idx][0],"[",
                endpoint = coref[s_id][w_idx][1]
            if endpoint == w_idx:
                print "]",
            print token.find("word").text,
        print


if __name__ == "__main__":
    with open("./data/out.xml", "r") as fi:
        tree = etree.parse(fi)
        coref_dict = replace_mention(tree)
        replace_by_coreference(tree, coref_dict)

