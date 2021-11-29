for i in range(1, 1000):
    x = i
    a, b = 0, 1
    m = x % 7
    while x > 0:
        d = x % 7
        if d > m:
            a += d
        else:
            b *= d
        x //= 7
    if a == 7 and b == 4:
        print(i)
        break
