def f(x, a):
    return not (0 <= x <= a) or ((8 <= x <= 20) or (15 <= x <= 75))


k = []

for a in range(1000):
    flag = True
    for x in range(1000):
        if f(x, a):
            flag = False
    if flag:
        k.append(a)

print(max(k))
