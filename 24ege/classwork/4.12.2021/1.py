f = open('files/24_1.txt', 'r').readline()

count = 0

for i in range(len(f) - 4):
    s = f[i] + f[i + 1] + f[i + 2] + f[i + 3] + f[i + 4]
    if s == s[::-1]:
        count += 1

print(count)
