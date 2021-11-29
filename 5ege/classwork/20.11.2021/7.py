for i in range(1, 1000):
    x = i
    a, b = 0, 0
    while x > 0:
        if x % 2 == 0:
            a += x % 7
        else:
            b += x % 7
        x //= 7
    if a == 4 and b == 2:
        print(i)
        break