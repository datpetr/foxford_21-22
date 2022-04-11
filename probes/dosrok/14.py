def x_to_n(x, n):
    s = ''
    while x:
        s += str(x % n)
        x //= n
    return s[::-1]


n = 3 * (16 ** 2018) - 2 * (8 ** 1028) - 3 * (4 ** 1100) - (2 ** 1050) - 2022

print(x_to_n(n, 4).count('3'))
print(x_to_n(n, 4))