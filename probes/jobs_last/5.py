def f(n):
    r = bin(n)[2:]
    r = r[1:]

    if r.count('1') % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '0'

    return int(r, 2)


a = []

for i in range(1, 10000):
    s = f(i)
    if s < 450:
        a.append(s)

print(max(a))
