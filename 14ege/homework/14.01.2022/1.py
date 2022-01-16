def x_to_n(x, n):
    st = ""
    while x:
        digit = x % n
        st += str(digit)
        x //= n

    return int(st[::-1])


expression = 343 ** 8 + 49 ** 2
mx = 0

for x in range(0, 10001):
    if str(x_to_n(expression - x, 7)).count('0') == 21 and x > mx:
        mx = x

print(mx)
