n = 500001
count = 0

while count < 5:
    d = []
    for i in range(18, n // 2 + 1, 10):
        if n % i == 0:
            print(n, i)
            count += 1
            break

    n += 1
