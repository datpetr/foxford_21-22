f = open('files/26.txt')

n = int(f.readline())
a = [[0] * 10002 for _ in range(10002)]

for _ in range(n):
    line, sq = map(int, f.readline().split())
    a[line][sq] = 1

f.close()
lines = [0] * 10001
count = 0
for l in range(1, 10000):
    amount = 0
    for s in range(1, 10000):
        if (a[l][s] + a[l][s + 1] +
                a[l + 1][s] + a[l + 1][s + 1] == 4
                and a[l - 1][s] + a[l - 1][s + 1] +
                + a[l][s - 1] + a[l][s + 2] +
                a[l + 1][s - 1] + a[l + 1][s + 2] +
                a[l + 2][s] + a[l + 2][s + 1] == 0):
            amount += 1

    count += amount
    lines[l] += amount
    lines[l + 1] += amount

print(count, lines.index(max(lines)))
