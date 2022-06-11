count = 0

for i in range(-1000, 1000):
    s = i
    p = 20
    q = 13
    k1 = k2 = 0
    while s < 230:
        s += p
        k1 += 1

    while s >= q:
        s -= q
        k2 += 1
    if k1 == 12 and k2 == 18:
        count += 1

print(count)
