def x_to_n(x, n):
    s = 0
    while x:
        s += x % n
        x //= n
    return s


n = 7 * (5 ** 1984) - 6 * (25 ** 777) + 5 * (125 ** 333) - 4

print(x_to_n(n, 5))