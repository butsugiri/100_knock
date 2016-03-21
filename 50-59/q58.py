# -*- coding: utf-8 -*-
"""
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．

msuzukiさんのパクリ…

実行例
python q58.py

output:
understanding	enabling	computers
others	involve	generation
Turing	published	article
experiment	involved	translation
ELIZA	provided	interaction
patient	exceeded	base
ELIZA	provide	response
which	structured	information
"""
import sys
from lxml import etree

def extract_tuples(tree):
    sent_deps = tree.xpath("//dependencies[@type='collapsed-dependencies']")
    for sent_dep in sent_deps:
        #述語候補のノードを抽出
        nsubj_nodes = sent_dep.xpath("dep[@type='nsubj']")
        for node in nsubj_nodes:
            #predicate(述語)のidxを使って，後に目的語を探す
            pre_idx = node.find("governor").attrib["idx"]
            pre_txt = node.find("governor").text

            #subject(主語)
            #xpathでnsubjを探索したので，子は絶対に主語になっている
            sub_txt = node.find("dependent").text

            query = "dep[@type='dobj']/governor[@idx='{}']".format(pre_idx)
            #目的語を探す
            #typeがdobj&&dobjとnsubjの親ノードであるようなノード
            obj_nodes = sent_dep.findall(query)
            if obj_nodes:
                obj_txt = obj_nodes[0].getnext().text
                print "{}\t{}\t{}".format(sub_txt,pre_txt,obj_txt)

if __name__ == "__main__":
    with open("./data/out.xml","r") as fi:
        tree = etree.parse(fi)
        extract_tuples(tree)
