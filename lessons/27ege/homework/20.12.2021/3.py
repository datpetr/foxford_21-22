f = open('files/3b.txt', 'r')

n = int(f.readline())

pairs = []
count = 0
md1 = md2 = md3 = md4 = md5 = md6 = md7 = 10001

for _ in range(n):
    k = list(map(int, f.readline().split()))
    k.sort(reverse=True)
    pairs.append(k)

print(pairs)

for i in pairs:
    count += i[0]
    s01 = i[0] - i[1]
    s02 = i[0] - i[2]
    if s01 % 8 == 1 and s01 < md1:
        md1 = s01
    if s01 % 8 == 2 and s01 < md2:
        md2 = s01
    if s01 % 8 == 3 and s01 < md3:
        md3 = s01
    if s01 % 8 == 4 and s01 < md4:
        md4 = s01
    if s01 % 8 == 5 and s01 < md5:
        md5 = s01
    if s01 % 8 == 6 and s01 < md6:
        md6 = s01
    if s01 % 8 == 7 and s01 < md7:
        md7 = s01

    if s02 % 8 == 1 and s02 < md1:
        md1 = s02
    if s02 % 8 == 2 and s02 < md2:
        md2 = s02
    if s02 % 8 == 3 and s02 < md3:
        md3 = s02
    if s02 % 8 == 4 and s02 < md4:
        md4 = s02
    if s02 % 8 == 5 and s02 < md5:
        md5 = s02
    if s02 % 8 == 6 and s02 < md6:
        md6 = s02
    if s02 % 8 == 7 and s02 < md7:
        md7 = s02

print(count, md1, md2, md3, md4, md5, md6, md7)
