for i in range(100000000000):
    s = i
    n = 50

    while n > 0:
        n = s // n
        s //= 2

    if s == 10000:
        print(i)
        break
