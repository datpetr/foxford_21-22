f = open('files/2b.txt', 'r')
n = int(f.readline())
s = 0
md1 = md2 = md3 = md4 = 10001
ans = []

for i in range(n):
    a, b = map(int, (f.readline().split()))
    s = s + max(a, b)
    if (abs(a - b)) % 5 == 1 and abs(a - b) < md1:
        md1 = abs(a - b)
    if (abs(a - b)) % 5 == 2 and abs(a - b) < md2:
        md2 = abs(a - b)
    if (abs(a - b)) % 5 == 3 and abs(a - b) < md3:
        md3 = abs(a - b)
    if (abs(a - b)) % 5 == 4 and abs(a - b) < md4:
        md4 = abs(a - b)

print(s, md1, md2, md3, md4)
f.close()
