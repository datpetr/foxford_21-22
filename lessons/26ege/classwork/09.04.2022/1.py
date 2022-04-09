f = open('files/26_1.txt', 'r')
n = int(f.readline())

a = []
for _ in range(n):
    pair = list(map(int, f.readline().split()))
    a.append(pair)

a.sort()
mx = r = m = 0
count = 1

for i in range(1, n):
    if a[i][0] == a[i - 1][0]:
        if a[i][1] - a[i - 1][1] == 1:
            count += 1
            if count >= mx:
                mx = count
                r = a[i][0]
                m = a[i][1]
        elif a[i][1] - a[i - 1][1] > 1:
            count = 1
    else:
        count = 1

print(mx, r, m)
