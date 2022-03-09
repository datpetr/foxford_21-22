def x_to_n(x, n):
    st = ''
    while x:
        st += str(x % n)
        x //= n
    return st[::-1]


print(x_to_n(3 ** 75 + 27 ** 17 + 9 ** 6 - 17, 3).count('2'), x_to_n(3 ** 75 + 27 ** 17 + 9 ** 6 - 17, 3))
