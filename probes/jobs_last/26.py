f = open('files/26.txt', 'r')

n = int(f.readline())
a = {}

for _ in range(n):
    s, d = list(map(int, f.readline().split()))
    s = s // 10 if s > 0 else -(abs(s) // 10)
    a[d] = a.get(d, []) + [s]

mc = md = 0
for d in sorted(a.keys()):
    if len(a[d]) > mc:
        mc = len(a[d])
        md = d

print(md, len(set(a[md])))
