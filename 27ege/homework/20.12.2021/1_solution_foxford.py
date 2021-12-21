F = open('filles/1A.txt', 'r')
n = int(F.readline())

s1 = 0
s2 = 0
md = n + 1

for i in range(n):
    a, b = map(int, (F.readline().split()))
    s1 += max(a, b)
    s2 += min(a, b)
    if (abs(a - b)) % 2 != 0:
        if abs(a - b) < md:
            md = abs(a - b)

if (s1 - s2) % 2 == 0:
    print(s1 - s2)
else:
    print(s1 - s2 - md)

F.close()
