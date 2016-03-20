# -*- coding: utf-8 -*-
"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""
import sys
from lxml import etree
from collections import defaultdict

def gather_coreference(tree):
    coref_nodes = tree.xpath("/root/document/coreference/coreference")
    coref_dict = defaultdict(lambda:defaultdict(int))
    for coref in coref_nodes:
        #Pathの指定で，"."を先頭につけることで，coref以下のみを探索
        me_nodes = coref.xpath("./mention")
        for me in me_nodes:
            if me.attrib.get("representative") == "true":
                rep = me.find("text").text
            else:
                s_id = int(me.find("sentence").text)
                start = int(me.find("start").text)
                end = int(me.find("end").text)
                coref_dict[s_id][start] = (rep,end)
    return coref_dict

def replace_by_coreference(tree,coref):
    endpoint = -1
    for sent in tree.xpath("//sentence[@id]"):
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
    with open("./data/out.xml","r") as fi:
        tree = etree.parse(fi)
        coref = gather_coreference(tree)
        replace_by_coreference(tree,coref)

