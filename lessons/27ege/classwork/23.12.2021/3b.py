f = list(map(int, open('files/27_3B.txt').readlines()))


n = f.pop(0)

mx = 0
length_mn = n + 1
sum_ = 0

a = []


for i in range(100):
    a.append([0] * 2)

for i in range(n):
    sum_ += f[i]
    r = sum_ % 100

    if r == 0:
        mx = sum_
        length_mn = i + 1
    elif a[r][0] != 0:
        if sum_ - a[r][0] > mx:
            mx = sum_ - a[r][0]
            length_mn = i - a[r][1]
        elif sum_ - a[r][0] > mx:
            if i - a[r][0] < length_mn:
                length_mn = i - a[r][0]

    if a[r][0] == 0:
        a[r][0] = sum_
        a[r][1] = i

print(mx, length_mn)
