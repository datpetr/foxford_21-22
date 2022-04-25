f = open('files/3b.txt', 'r')

n = int(f.readline())
mn_numb = 10001
s = 0

for _ in range(n):
    d = list(map(int, f.readline().split()))
    d.sort(reverse=True)
    s += d[0]
    mn = min(d[0] - d[1], d[0] - d[2])
    if mn < mn_numb and mn % 4 != 0:
        mn_numb = mn

if s % 4 == 0:
    print(s - mn_numb)
else:
    print(s)

print(s, mn)
