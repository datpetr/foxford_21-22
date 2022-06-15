for i in range(1000):
    x = i
    k = 9 * x - 57
    d = 9 * x + 13
    while k * d > 0:
        if k > d:
            k %= d
        else:
            d %= k

    if k + d == 70:
        print(i)
