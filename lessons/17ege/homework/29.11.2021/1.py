f = list(map(int, open('files/1.txt', 'r').readlines()))

count = 0
mx = 0

for i in range(len(f) - 2):
    if f[i] < f[i + 1] < f[i + 2]:
        count += 1
        if f[i] + f[i + 1] + f[i + 2] > mx:
            mx = f[i] + f[i + 1] + f[i + 2]

print(count, mx)
