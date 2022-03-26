f = open('files/27_4b.txt', 'r')

n = int(f.readline())
m12 = 10 ** 10
m21 = 10 ** 10
m11 = 10 ** 10
smn = 0
smx = 0

for i in range(n):
    x, y = list(map(int, f.readline().split()))

    if x % 2 != 0:
        smn += min(y, x)
        smx += max(x, y)

        if max(x, y) % 2 != 0 and min(x, y) % 2 == 0:
            m12 = min(m12, x + y)
        if max(x, y) % 2 == 0 and min(x, y) % 2 != 0:
            m21 = min(m21, x + y)
        if max(x, y) % 2 != 0 and min(x, y) % 2 != 0:
            m11 = min(m11, x + y)

print(smx, smn, m11, m12, m21)
if smx % 2 != 0 and smn % 2 == 0:
    print(smx + smn)
if smx % 2 == 0 and smn % 2 != 0:
    print(smn + smx - m11)
if smx % 2 != 0 and smn % 2 != 0:
    print(smn + smx - m21)
if smx % 2 == 0 and smn % 2 == 0:
    print(smn + smx - m12)

f.close()
