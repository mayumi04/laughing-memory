f = open('input.txt', 'w', encoding = 'utf_8')
x = input('文字を入力。') + '\n'
while x != 'exit\n':
    f.writelines(x)
    x = input('文字を入力。') + '\n'
f.close()