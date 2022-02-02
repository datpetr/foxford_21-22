start, end = 1000000, 2000000

divCount = 5

for num in range(start, end + 1):
    d = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and i % 2 == 0:
            if i != (num // i):
                d.append(i)
                d.append(num // i)
            else:
                d.append(i)

    if len(d) == divCount:
        print(num)

