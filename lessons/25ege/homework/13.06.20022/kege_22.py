def f(n):
    a = []
    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i == i:
                a.append(i)
                count += 1
            else:
                a.extend([i, n // i])
                count += 2

    if count == 2:
        return a


for i in range(174457, 174506):
    s = f(i)
    if s is not None:
        print(s)
