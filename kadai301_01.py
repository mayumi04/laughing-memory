class total():
    l = []
    print(f'合計：{sum(l)}')
    x = input()
    
    while x.isdigit():
        l.append(int(x))
        print(f'合計：{sum(l)}')
        x = input()
    else:
        print('終わります。')