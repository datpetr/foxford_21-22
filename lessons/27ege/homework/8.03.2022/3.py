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

F.close()
