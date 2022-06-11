def f(n):
    n_2 = bin(n)[2:]

    if int(n_2) % 2 == 0:
        n_2 = '1' + n_2 + '0'
    else:
        n_2 = '11' + n_2 + '11'

    return int(n_2, 2)


a = []
for i in range(1000):
    s = f(i)
    if s > 52:
        a.append(s)
print(min(a))