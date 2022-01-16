def x_to_n(x, n):
    st = ""
    while x:
        digit = x % n
        st += str(digit)
        x //= n

    return int(st[::-1])


expression = 16 ** 8 + 2 ** 8
mn = 10001

for x in range(0, 10001):
    if str(x_to_n(expression - x, 4)).count('3') == 12 and x < mn:
        mn = x

print(mn, x_to_n(expression - mn, 4))
