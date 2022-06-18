for i in range(10000000000):
    s = i
    k1 = k2 = 0

    while s > 0:
        d = s % 10
        if d > 5:
            s -= 1
            k1 += 1
        else:
            s //= 10
            k2 += 1

    if k1 + k2 == 58:
        print(i)
        break
