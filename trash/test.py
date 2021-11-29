k = []
for x in range(1, 1000):
    for y in range(1, 1000):
        if ((x ** 2) - (y ** 2) + x - (2 * y) + 9) == 0:
            k.append(abs(x - y))

print(max(k))
