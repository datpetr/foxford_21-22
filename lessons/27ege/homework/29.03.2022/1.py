f = open('files/1b.txt', 'r')
n = int(F.readline())
s = 0
md = 100001

for _ in range(n):

    d = list(map(int, (f.readline().split())))
    d.sort(reverse=True)
    s += d[0]

    if (abs(d[0] - d[1])) % 4 != 0 and abs(d[0] - d[1]) < md:
            md = abs(d[0] - d[1])


if s % 4 != 0:
    print(s)
else:
    print(s - md)

f.close()
