def f(x, a):
    return 144 % a == 0 and ((x % a != 0) <= ((x % 18 == 0) <= (x % 24 != 0)))


k = []

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not (f(x, a)):
            flag = False

    if flag:
        k.append(a)

print(max(k))
