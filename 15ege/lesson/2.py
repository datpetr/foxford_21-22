def f(x, y, a):
    return (6 * y - 2 * x) > a or (x + 4 * y) < 80 or (2 * y - 3 * x) < -72


k = []

for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not(f(x, y, a)):
                flag = False
    if flag:
        k.append(a)

print(max(k))
