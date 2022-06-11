def x_to_n(x, n):
    s = ''
    while x:
        s += str(x % n)
        x //= n
    return s[::-1]


count = 0
n = 7 * (5 ** 1984) - 6 * (25 ** 777) + 5 * (125 ** 333) - 4
for i in x_to_n(n, 7):
    count += int(i)

print(count)