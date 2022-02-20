F = open('files/3a.txt', 'r')

n = int(F.readline())
s = 0
md1 = md2 = md3 = md4 = md5 = md6 = md7 = 10001
ans = []

for _ in range(n):
    a, b, c = map(int, (F.readline().split()))
    s += max(a, b, c)

    if (abs(a - b)) % 8 == 1 and abs(a - b) < md1:
        md1 = abs(a - b)
    if (abs(a - b)) % 8 == 2 and abs(a - b) < md2:
        md2 = abs(a - b)
    if (abs(a - b)) % 8 == 3 and abs(a - b) < md3:
        md3 = abs(a - b)
    if (abs(a - b)) % 8 == 4 and abs(a - b) < md4:
        md4 = abs(a - b)
    if (abs(a - b)) % 8 == 5 and abs(a - b) < md5:
        md4 = abs(a - b)
    if (abs(a - b)) % 8 == 6 and abs(a - b) < md6:
        md4 = abs(a - b)
    if (abs(a - b)) % 8 == 7 and abs(a - b) < md7:
        md4 = abs(a - b)

    if (abs(a - c)) % 8 == 1 and abs(a - c) < md1:
        md1 = abs(a - c)
    if (abs(a - c)) % 8 == 2 and abs(a - c) < md2:
        md2 = abs(a - c)
    if (abs(a - c)) % 8 == 3 and abs(a - c) < md3:
        md3 = abs(a - c)
    if (abs(a - c)) % 8 == 4 and abs(a - c) < md4:
        md4 = abs(a - c)
    if (abs(a - c)) % 8 == 5 and abs(a - c) < md5:
        md4 = abs(a - c)
    if (abs(a - c)) % 8 == 6 and abs(a - c) < md6:
        md4 = abs(a - c)
    if (abs(a - c)) % 8 == 7 and abs(a - c) < md7:
        md4 = abs(a - c)

print(s, md1, md2, md3, md4, md5, md6, md7)

if (s - md1) % 8 == 0:
    ans.append(s - md1)
if (s - md2) % 8 == 0:
    ans.append(s - md2)
if (s - md3) % 8 == 0:
    ans.append(s - md3)
if (s - md4) % 8 == 0:
    ans.append(s - md4)
if (s - md5) % 8 == 0:
    ans.append(s - md5)
if (s - md6) % 8 == 0:
    ans.append(s - md6)
if (s - md7) % 8 == 0:
    ans.append(s - md7)

print(max(ans))

F.close()
