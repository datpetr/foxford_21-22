def f(x, a):
    return (x & 23 != 0 or x & 10 != 0) <= ((x & 1 == 0) <= (x & a != 0))


k = []

for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        if not (f(x, a)):
            flag = False

    if flag:
        k.append(a)

print(min(k))
