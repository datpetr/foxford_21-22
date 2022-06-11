f = list(map(int, open('files/17.txt', 'r').readlines()))

average = sum(f) / len(f)
count = mx_pair = 0
for i in range(1, len(f) - 2):
    if (f[i] * f[i + 1]) >= (f[i - 1] * f[i + 2]) and (f[i] > average or f[i + 1] > average):
        count += 1
        if f[i] + f[i + 1] > mx_pair:
            mx_pair = f[i] + f[i + 1]

print(count, mx_pair)
