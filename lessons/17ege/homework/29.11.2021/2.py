f = list(map(int, open('files/2.txt', 'r').readlines()))

count = 0
mx = 0

for i in range(len(f) - 3):
    if f[i] + f[i + 1] + f[i + 2] + f[i + 3] > mx:
        mx = f[i] + f[i + 1] + f[i + 2] + f[i + 3]


for i in range(len(f) - 3):
    if f[i] + f[i + 1] + f[i + 2] + f[i + 3] == mx:
        count += 1

print(mx, count)
