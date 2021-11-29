def f(x, y, a):
    return y >= 2 * x or x >= 15 or (x + 2 * y) < a


k = []

for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not(f(x, y, a)):
                flag = False
    if flag:
        k.append(a)

print(min(k))
