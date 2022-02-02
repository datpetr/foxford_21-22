for n in range(1, 1000):
    s = bin(n)[2:]
    s += s[-1]
    if len(s) % 2 == 0:
        s += '0'
    else:
        s += '1'
    while s.count('1') % 2 != 0:
        if len(s) % 2 == 0:
            s += '0'
        else:
            s += '1'

    print(int(s, 2))
