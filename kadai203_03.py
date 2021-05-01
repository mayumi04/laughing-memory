i = 1
y = 1

while True:
    x = 2 ** i
    y = len(str(x))
    if y == 10:
        break
    else:
        print(x)
        i += 1