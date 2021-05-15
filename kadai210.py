import collections
import re

with open('bible.txt', 'r') as bible:
    text = bible.read()
    # bible.txtを単語で分割する
t = re.split(r'[^a-zA-Z]+', text)


# 1.指定した英単語の出現数を出力
word = input('探したい単語を入力：')
count = t.count(word)
if count == 0:
    print('その単語はありません。')
else:    
    print(f'{word}は{count}回')

# 2.英単語の出現数ランキングを出力
x = input('単語出現ランキングの表示順位を入力：')

if re.fullmatch('[0-9]+', x) :
    num = int(x)
    n = num + 1
    c = collections.Counter(t)
    rank = c.most_common(n)
    for i in range(0, num):
        print(f'{i+1:>3}位{rank[i][0]:>10}: {rank[i][1]:4}回')
else:
    print("ランキングは半角数字で入力してください。")