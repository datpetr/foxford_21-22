for i in range(1, 1000):
    n = i
    count = 0
    s = bin(n)[2:]
    for j in s:
        count += int(j)
