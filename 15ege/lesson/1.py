def F(x, a):
    return x % a == 0 or x % 6 != 0 or x % 9 != 0


k = []

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not(F(x, a)):
            flag = False
    if flag:
        k.append(a)

print(max(k))
