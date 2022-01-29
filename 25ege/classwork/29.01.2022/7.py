def sl(n):
    d = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i ** 2 != n:
                d.append(i)
                d.append(n // i)
            else:
                d.append(i)
    d.sort()
    return d


x = 200000001
count = 0
p = 0


while count < 5:
    a = sl(x)
    if len(a) >= 5:
        for i in range(5):
            p *= a[i]
        if p < x and p % 10 == 1:
            count += 1
            print(x, p, a[4])
    x += 1
