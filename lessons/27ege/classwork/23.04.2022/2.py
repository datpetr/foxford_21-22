f = list(map(int, open('files/27_2b.txt', 'r').readlines()))

n = f.pop(0)
s = count = 0
a = [0] * 2022

for i in range(n):
    x = f[i]
    s += x
    if s % 2022 == 0:
        a[0] += 1
        count += a[0]
    else:
        count += a[s % 2022]
        a[s % 2022] += 1

print(count)
