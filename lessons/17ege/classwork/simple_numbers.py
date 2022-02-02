def fact(n):
    k = []
    k2 = []
    k3 = []
    d = 2
    count = 1
    k.append(-1)
    while d ** 2 <= n:
        if n % d == 0:
            k.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        k.append(n)
    for i in range(1, len(k)):
        if k[i] != k[i - 1]:
            k2.append(k[i])
            k2.append(k.count(k[i]))
            k3.append(k2)
            k2 = []
            count = 1
    return k3


print(fact(int(input())))
