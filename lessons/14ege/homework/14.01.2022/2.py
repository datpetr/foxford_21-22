def x_to_n(x, n):
    st = ""
    while x:
        digit = x % n
        st += str(digit)
        x //= n

    return int(st[::-1])


expression = 125 ** 10 + 25 ** 2
mn = 10001

for x in range(0, 10001):
    if str(x_to_n(expression - x, 5)).count('4') == 27 and x < mn:
        mn = x

print(mn, x_to_n(expression - mn, 5))
