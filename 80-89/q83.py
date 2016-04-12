# -*- coding: utf-8 -*-
"""
83. 単語／文脈の頻度の計測
"""
import sys
from collections import defaultdict

def main(fi):
    fo1 = open("/work/kiyono/f_tc.txt","w")
    fo2 = open("/work/kiyono/f_t.txt","w")
    fo3 = open("/work/kiyono/f_c.txt","w")
    f_tc = defaultdict(int)
    f_t = defaultdict(int)
    f_c = defaultdict(int)
    for line in fi:
        target,context = line.rstrip().split("\t",1)
        contexts = context.split("\t")
        f_t[target] += 1
        for c in contexts:
            f_c[c] += 1
            f_tc[(target,c)] += 1

    print "N = {}".format(len(f_tc))
    print "f_tc.txt working..."
    for word,count in f_tc.iteritems():
        target = word[0]
        context = word[1]
        fo1.write("{}\t{}\t{}\n".format(target,context,count))

    print "f_t.txt working..."
    for k,v in f_t.iteritems():
        fo2.write("{}\t{}\n".format(k,v))

    print "f_c.txt working..."
    for k,v in f_c.iteritems():
        fo3.write("{}\t{}\n".format(k,v))

    fo1.close()
    fo2.close()
    fo3.close()


if __name__ == "__main__":
    main(sys.stdin)
