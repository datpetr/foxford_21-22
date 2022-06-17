count = 0

for i in range(-10000, 10000):
    p = 12
    q = 8
    k1 = k2 = d = 0
    s = i
    s += 21

    while s >= 43:
        s -= 43
        d += 1

    while s < 0:
        s += 43
        d -= 1

    while d <= 100:
        d += p
        k1 += 1

    while d >= q:
        d -= q
        k2 += 1

    k1 += d
    k2 += d

    if k1 == 13 and k2 == 17:
        count += 1

print(count)
