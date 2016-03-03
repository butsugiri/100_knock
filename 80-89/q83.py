# -*- coding: utf-8 -*-
"""
83. 単語／文脈の頻度の計測
"""
import sys
from collections import defaultdict

def main(fi):
    fo1 = open("./data/f_tc.txt","w")
    fo2 = open("./data/f_t.txt","w")
    fo3 = open("./data/f_c.txt","w")
    f_tc = defaultdict(lambda: defaultdict(int))
    f_t = defaultdict(int)
    f_c = defaultdict(int)
    for line in fi:
        t,c = line.rstrip().split("\t")
        f_tc[t][c] += 1
        f_t[t] += 1
        f_c[c] += 1

    print "N = {}".format(len(f_tc))
    print "f_tc.txt working..."
    for k in f_tc.iterkeys():
        for t,c in f_tc[k].iteritems():
            fo1.write("{} {}\t{}\n".format(k,t,c))

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
