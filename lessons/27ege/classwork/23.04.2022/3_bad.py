f = list(map(int, open('files/27_3a.txt', 'r').readlines()))

n = f.pop(0)

count = s = 0

for i in range(n - 22):
    s = 0
    for j in range(i, n):
        s += f[j]
        if s % 2022 == 0 and j - i > 22:
            count += 1

print(count)
