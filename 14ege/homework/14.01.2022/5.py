def x_to_n(x, n):
    st = ""
    dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    while x:
        digit = x % n
        if digit > 9:
            st += dict[digit]
        else:
            st += str(digit)
        x //= n

    return st[::-1]


for x in range(1, 10000):
    if len(x_to_n(x, 6)) == 2 and len(x_to_n(x, 5)) == 3 and x_to_n(x, 11)[-1] == '1':
        print(x)
        break
