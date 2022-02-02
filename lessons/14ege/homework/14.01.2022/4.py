def x_to_n(x, n):
    st = ""
    while x:
        digit = x % n
        st += str(digit)
        x //= n

    return st[::-1]


expression = 6 * (343 ** 1156) - 5 * (49 ** 1147) + 4 * (7 ** 1153) - 875

expression_7 = x_to_n(expression, 7)
sum_ = 0

for i in expression_7:
    sum_ += int(i)

print(sum_)
