def f(num, d=2):
    a = []
    while num > 1:
        n1, n2 = divmod(num, d)
        if n2:
            d += 1
        else:
            a.append(d)
            num = n1
    return a


numbers = []
n = 250000

while len(numbers) < 5:
    a = f(n)
    if bool(a) and sum(a) % 17 == 0:
        numbers.append([n, sum(a)])
    n += 1

numbers.sort()
print(*numbers)
