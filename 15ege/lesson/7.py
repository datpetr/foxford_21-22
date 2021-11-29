def f(x, a):
    return a % 9 == 0 and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))


k = []

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not (f(x, a)):
            flag = False

    if flag:
        k.append(a)

print(min(k))
