f = list(map(int, open('files/17_1.txt', 'r').readlines()))

average = 0
mx = 0
count = 0

average = sum(f) / len(f)

for i in range(len(f) - 1):
    if ((f[i] > average > f[i + 1]) or
            (f[i] < average < f[i + 1])):
        count += 1
        if mx < (f[i] + f[i + 1]):
            mx = (f[i] + f[i + 1])

print(count, mx)
