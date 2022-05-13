def f(n):
    n_2 = bin(n)[2:]
    if int(n_2) % 2 == 0:
        n_2 = '10' + n_2
    else:
        n_2 = '1' + n_2 + '01'

    return int(n_2, 2)


for i in range(1, 10000):
    s = f(i)
    print(s)
    if f(i) >= 19:
        print(i)
        break
