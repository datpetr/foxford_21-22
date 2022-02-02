max = 0

for i in range(1000):

    w = i
    w -= 2
    n = 1

    while w < 120:
        w = w + 7
        n = n * 2 + 2

    if n == 94:
        mx = i

print(mx)
