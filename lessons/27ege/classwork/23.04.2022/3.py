f = list(map(int, open('files/27_3b.txt', 'r').readlines()))

n = f.pop(0)
s = count = 0
a = [0] * 2022
b = [0]

for i in range(23):
    s += f[i]
    b.append(s)

for i in range(23, n):
    a[b[0] % 2022] += 1
    x = f[i]
    s += x
    r = s % 2022
    count += a[r]
    for j in range(23):
        b[j] = b[j + 1]
    b[23] = s

print(count)
