# -*- coding: utf-8 -*-
"""
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
"""
import sys

def main(fi):
    family_section = False
    for line in fi:
        if family_section and line.startswith(":"):
            break
        elif family_section:
            sys.stdout.write(line)
        elif line.startswith(": family"):
            family_section = True

if __name__ == "__main__":
    main(sys.stdin)
