def f(n):
    n_2 = bin(n)[2:]
    if int(n_2) % 2 == 0:
        n_2 = '1' + n_2 + '00'
    else:
        n_2 = '10' + n_2 + '1'

    return int(int(n_2, 2))


mx = 0

for i in range(1, 10000):
    if f(i) < 1000 and mx < i:
        mx = i
        print(i)

print(mx)
