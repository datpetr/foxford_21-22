def dell(n, m):
    return n % m == 0


for a in range(1000):
    for x in range(10000):
        if not((dell(x, 6) <= (not dell(x, 14))) or ((x + a) >= 70) and dell(a, 20)):
            break
    else:
        print(a)
        break
