def f(n):
    if n == 0:
        return 1
    if n > 0 and n % 5 == 0:
        return n / 5 + f(n / 5)
    if n > 0 and (n % 5 > 0):
        return n % 5 + f(n - 1)


for i in range(1, 10000):
    if f(i) == 2021:
        print(i)
        break
