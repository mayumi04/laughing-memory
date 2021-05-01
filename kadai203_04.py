plus = 20000  * 12     #1年で貯金する額
nen = 100000    #初期値は元本

for y in range(1, 11):
    tyokin = 100000 + plus * y
    unyou = round((nen + plus) *1.07)
    print("{:2}年目　{:>9,}円　{:>9,.0f}円".format(y, tyokin, unyou))  
    nen = unyou