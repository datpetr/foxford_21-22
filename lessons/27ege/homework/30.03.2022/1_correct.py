F = open('files/1b.txt', 'r')
n = int(F.readline())
s = 0
md = 100001

for _ in range(n):

    d = list(map(int, (F.readline().split())))
    d.sort(reverse=True)
    s += d[0]

    if (abs(d[0] - d[1])) % 5 != 0 and abs(d[0] - d[1]) < md:
            md = abs(d[0] - d[1])
    if (abs(d[0] - d[2])) % 5 != 0 and abs(d[0] - d[2]) < md:
            md = abs(d[0] - d[2])

if s % 5 != 0:
    print(s)
else:
    print(s - md)
F.close()
