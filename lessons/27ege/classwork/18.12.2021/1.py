f = open('files/27_1.txt', 'r').readlines()

n = int(f.pop(0))
md = n + 1

k = []
s = 0

for i in f:
    a, b = map(int, i.split())
    s += max(a, b)
    if abs(a - b) < md and abs(a - b) % 5 != 0:
        md = abs(a - b)

if s % 5 != 0:
    print(s)
else:
    print(s - md)
