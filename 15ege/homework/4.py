def f(x, y, a):
    return (y + 3 * x < a) or (x > 20) or (y > 40)


k = []

for a in range(300):
    flag = True
    for x in range(300):
        for y in range(300):
            if not (f(x, y, a)):
                flag = False

    if flag:
        k.append(a)

print(min(k))
