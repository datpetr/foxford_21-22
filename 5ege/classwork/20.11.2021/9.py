for i in range(6, 100):
    x = i
    a = 7 * x + 13
    b = 7 * x - 35
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 24:
        print(i)
        break
