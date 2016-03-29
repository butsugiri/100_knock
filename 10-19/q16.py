# -*- coding: utf-8 -*-
"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

実行例:
python 016.py 3 hoge data/hightemp.txt

UNIX:
split -d -n l/4 ./data/hightemp.txt ./data/hightemp.txt
-dでnumeric suffixを指定
-nで分割数を指定(GNU版onlyなオプション?)
l/Nとしてやることで，行の途中で分割されるのを防ぐ
(今回は行単位で分割したい)

"""
import sys

def lineInEachTxt(total_ln, N, n):
    div = total_ln / N
    remainder = total_ln % N
    if remainder > n:
        return div + 1
    else:
        return div

def main(inp,N,fname):
    with open(inp,"r") as f:
        total_ln = sum(1 for i in f)
        f.seek(0) #i.e. ファイルを再オープン
        for n in range(N):
            with open(fname + str(n),"w") as fo:
                for n, line in zip(range(lineInEachTxt(total_ln, N, n)), f):
                    fo.write(line)

if __name__ == "__main__":
    N = int(sys.argv[1])
    output_name = sys.argv[2]
    inp = sys.argv[3]
    main(inp,N,output_name)
