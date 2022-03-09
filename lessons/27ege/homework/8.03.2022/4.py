f = open('files/4b.txt', 'r')

n = int(f.readline())

pairs = []
count = 0
md1 = md2 = md3 = md4 = md5 = md6 = md7 = md8 = md9 = md10 = 10001

for _ in range(n):
    k = list(map(int, f.readline().split()))
    k.sort(reverse=True)
    pairs.append(k)


for i in pairs:

    count += i[2]
    s01 = i[1] - i[2]
    s02 = i[0] - i[2]

    if s01 % 11 == 1 and s01 < md1:
        md1 = s01
    if s01 % 11 == 2 and s01 < md2:
        md2 = s01
    if s01 % 11 == 3 and s01 < md3:
        md3 = s01
    if s01 % 11 == 4 and s01 < md4:
        md4 = s01
    if s01 % 11 == 5 and s01 < md5:
        md5 = s01
    if s01 % 11 == 6 and s01 < md6:
        md6 = s01
    if s01 % 11 == 7 and s01 < md7:
        md7 = s01
    if s01 % 11 == 8 and s01 < md8:
        md8 = s01
    if s01 % 11 == 9 and s01 < md9:
        md9 = s01
    if s01 % 11 == 10 and s01 < md10:
        md10 = s01

    if s02 % 11 == 1 and s02 < md1:
        md1 = s02
    if s02 % 11 == 2 and s02 < md2:
        md2 = s02
    if s02 % 11 == 3 and s02 < md3:
        md3 = s02
    if s02 % 11 == 4 and s02 < md4:
        md4 = s02
    if s02 % 11 == 5 and s02 < md5:
        md5 = s02
    if s02 % 11 == 6 and s02 < md6:
        md6 = s02
    if s02 % 11 == 7 and s02 < md7:
        md7 = s02
    if s02 % 11 == 8 and s02 < md8:
        md8 = s02
    if s02 % 11 == 9 and s02 < md9:
        md9 = s02
    if s02 % 11 == 10 and s02 < md10:
        md10 = s02

print(count, md1, md2, md3, md4, md5, md6, md7, md8, md9, md10)
