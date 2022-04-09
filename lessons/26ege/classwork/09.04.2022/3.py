f = open('files/26_3.txt', 'r')

n, ts = map(int, f.readline().split())
a = []
tf = ts + 3600 * 24 * 1000

for _ in range(n):
    s, g = map(int, f.readline().split())
    a.append([s, 1])
    if f == 0:
        f = tf
    a.append([f, -1])

a.sort()

count = 0
mx = 0
for i in range(len(a)):
    count += a[i][1]
    if ts <= a[i][0] <= tf:
        pass
