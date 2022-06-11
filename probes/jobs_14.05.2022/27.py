from math import ceil


f = open('files/27-B.txt', 'r')

n, k = map(int, f.readline().split())
a = list(map(int, f.readlines()))
f.close()

s = mx = 0

for x in a:
    if x > 0:
        s += x
    else:
        if s + x > 0:
            s += x
        else:
            s = 0
    mx = max(mx, ceil(s // k))

print(mx)