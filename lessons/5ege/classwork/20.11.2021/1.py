k = []
for i in range(1, 2021):
    s = i
    s //= 5
    s += 50
    n = 0
    while s < 2021:
        s += 5 * n
        n += 5
    if n == 70:
        k.append(i)

print(max(k))
