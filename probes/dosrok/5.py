def f(n):
    n_2 = int(bin(n)[2:])
    if n_2 % 2 == 0:
        n_2 = str(n_2) + '10'
    else:
        n_2 = '1' + str(n_2) + '01'

    return int(int(n_2, 2))


for i in range(1, 10000):
    if f(i) >= 516:
        print(i)
        break
