"""
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．

grep -v "@classias" model_baseline.txt |grep -v "__BIAS__" | sort -g -r|head
1.75073	refresh
1.48785	engross
1.44098	unexpect
1.33345	remark
1.26236	glorious
1.25863	solid
1.24668	beauti
1.21772	examin
1.19595	quiet
1.18665	delight

grep -v "@classias" model_baseline.txt|grep -v "__BIAS__" | sort -g|head
-1.87926	bore
-1.73661	dull
-1.61029	fail
-1.49151	neither
-1.47468	wast
-1.45928	worst
-1.42658	mediocr
-1.42503	bad
-1.395	flat
-1.35425	routin
"""
# grep -v はinVert matchの意
