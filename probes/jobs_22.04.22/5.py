def f(n):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r + '00'
    else:
        r = '11' + r

    return int(r, 2)


for i in range(10000):
    s = f(i)
    if s >= 412:
        print(i)
        break
