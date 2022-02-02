def x_to_10(x, n):
    st = str(x)[::-1]

    k = []
    res = 0

    dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    for i in range(len(st)):
        if st[i] in dict:
            res += int(dict[st[i]]) * (n ** i)
        else:
            res += int(st[i]) * (n ** i)

    return res


for x in range(16):
    if x_to_10(441, x) + 14 == x_to_10(252, 7):
        print(x)
        break
