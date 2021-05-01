c1 = 100
c2 = 300
n = 25

g = c1 * n + c2 * n
goukei = '{:,}'.format(g)

print(str(c1)+ "円のバナナを" + str(n)  + "個、"
     + str(c2) + "円の桃を" + str(n) + "個買ったら、合計"
     + goukei + "円になりました。")

# 203_04
print("{}円のバナナを{}個、{}円の桃を{}個買ったら、合計{}円になりました。"
     .format(c1, n, c2, n, goukei))
