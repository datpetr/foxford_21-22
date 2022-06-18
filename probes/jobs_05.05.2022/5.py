def f(n):
    r = bin(sum([int(x) for x in str(n)]))[2:]

    if r.count('1') % 2 == 0:
        r = '1' + r + '00'
    else:
        r = '10' + r + '1'

    return int(r, 2)


count = 0

for i in range(10000):
    if f(i) == 21:
        count += 1
        

print(count)
