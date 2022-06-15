def divors(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i == i:
                a.append(i)
            else:
                a.append(n // i)
                a.append(i)

    a.sort()
    return a


n = 800_000
amount_answers = 0
while amount_answers != 6:
    s = divors(n)
    count = 1

    for i in s:
        count *= i

    if sum(s) % 2 != 0 and count % 2 != 0 and len(s) > 10:
        print(n, len(s))
        amount_answers += 1
    n += 1