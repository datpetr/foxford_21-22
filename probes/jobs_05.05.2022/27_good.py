f = open('files/27-B.txt', 'r')

n, k = map(int, f.readline().split())
a = list(map(int, f.readlines()))[:n] * 2

st = s = 0
mc = 10 ** 10
for i in range(n):
    s += a[i]
    while s > k:
        s -= a[st]
        st += 1
    if s == k:
        if mc > i - st + 1:
            mc = i - st + 1
        s -= a[st]
        st += 1

print(mc)
