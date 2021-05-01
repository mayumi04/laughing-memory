#石なし=0、
#○=1
#●=2

from collections import Counter

l = [[1,1,1,1,1],
    [0,0,2,1,0],
    [0,2,1,2,2],
    [0,2,0,2,0],
    [0,0,0,0,2]]

l2 = []
for i in l:
    for j in i:
        l2.append(j)

cnt1 = l2.count(1)
print("○：" + str(cnt1) + "個")

cnt2 = l2.count(2)
print("●：" + str(cnt2) + "個")

win = cnt1 - cnt2
if win > 0:
    print("○の勝ち")
elif win < 0:
    print("●の勝ち")
else:
    print("引き分け")

