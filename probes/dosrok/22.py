for i in range(1000):
    s = i
    p = 10
    q = 8
    k1 = 0
    k2 = 0
    while s <= 100:
        s += p
        k1 += 1

    while s >= q:
        s -= q
        k2 += 1

    k1 += s
    k2 += s
    if k1 == 10 and k2 == 19:
        print(i)
        break
