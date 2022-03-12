def x_to_n(x, n):
    st = ''
    while x:
        st += str(x % 7)
        x //= n
    return st[::-1]


f = list(map(int, open('17_7.txt', 'r').readlines()))

mx_elem = -1
mn = 100000
count = 0

for i in f:
    if i > mx_elem and i % 107 == 0:
        mx_elem = i

for i in range(len(f) - 1):
    if ((f[i] > mx_elem or f[i + 1] > mx_elem)
            and ('36' in x_to_n(f[i], 7) or ('36' in x_to_n(f[i + 1], 7)))):
        count += 1
        if (f[i] + f[i + 1]) < mn:
            mn = f[i] + f[i + 1]

print(mn, count)
