def f(n):
    r = bin(n)[2:]
    count = sum([int(i) for i in r])
    for _ in range(2):
        r = r + str(count % 2)

    return int(r, 2)


for i in range(1000):
    if f(i) > 43:
        print(f(i))
        break
