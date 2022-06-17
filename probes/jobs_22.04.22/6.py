for i in range(10000):
    s = i
    s = (s + 31) // 26
    n = 813

    while s > 0:
        n = n // 3
        s -= n

    if n == 30:
        print(i)
        break
