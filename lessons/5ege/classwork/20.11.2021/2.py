k = []
for i in range(1, 2021):
    s = i
    n = 1
    while s < 31:
        s += 3
        n *= 2
    if n == 128:
        k.append(i)

print(min(k))
