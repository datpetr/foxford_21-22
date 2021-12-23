f = open('files/3.txt', 'r')

n = int(f.readline())
k = []
r = 0
m = 0

for i in range(n):
    pair = list(map(int, f.readline().split()))
    k.append(pair)

k.sort(key=lambda a: (a[0], -a[1]))

for i in range(n - 1):
    if k[i][0] == k[i + 1][0] and (k[i][1] - k[i + 1][1]) == 6:
        r = k[i][0]
        m = k[i + 1][1]

print(r, m + 1)
f.close()
