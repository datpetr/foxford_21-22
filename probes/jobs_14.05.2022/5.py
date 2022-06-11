def f(n):
    n_2 = bin(n)[2:]
    if int(n_2) % 2 != 0:
        n_2 = '1' + n_2 + '00'
    else:
        n_2 = '11' + n_2 + '0'
    return int(n_2, 2)


a = [-1] * (10 ** 5)
count = [0] * (10 ** 5)

for i in range(256):
    s = f(i)
    if a[s] == -1:
        a[s] = s
    elif s in a:
        count[s] += 1

print(sum(count) - 1)
