for i in range(1, 1000):
    x = i
    a, b = 0, 0
    while x > 0:
        d = x % 10
        if d > 5:
            a += 1
        if d < 8:
            b += 1
        x //= 10
    if a == 3 and b == 2:
        print(i)
        break
