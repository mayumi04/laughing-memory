i = 1

while i < 4:
    key = input("ひらがなを入力してください。")

    karuta = {
        "い": "犬も歩けば棒に当たる", 
        "ろ": "論より証拠",
        "は": "花より団子",

    }

    if key in karuta:
        print(karuta[key])
    else:
        print("そんなのないよ！")
        break
    
    i += 1
