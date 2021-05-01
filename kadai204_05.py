n = input("整数を入力してください。")

n_int = int(n) 
pikon = []      #ピコン！のカウンター

#１から整数ｎを順番にｘに入れて見ていく
for x in range(1, n_int + 1):
    str_x = str(x)
    new_str = str_x[::-1]       #ｘを逆さまにする　10 -> 01
    new_int = int(new_str)      #01 -> 1

    #逆さまに読むとｎより大きい場合は”ピコン！”と出力する
    if new_int > n_int:
        print(str(x) + " -> " + str(new_int) +" ピコン！")
        pikon.append(new_str)       #ピコン！のカウンターに追加
    else:
        print(str(x) + " -> " + str(new_int))

print(len(pikon))