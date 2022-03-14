f = list(map(int, open('2.txt', 'r').readlines()))

count = 0
average = sum(f) / len(f)
mx = 0

for i in range(len(f) - 1):
    if abs(f[i] - f[i + 1]) <= 20 and f[i] + f[i + 1] > average:
        count += 1
        if f[i] + f[i + 1] > mx:
            mx = f[i] + f[i + 1]

print(count, mx)
