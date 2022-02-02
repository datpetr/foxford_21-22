f = list(map(int, open('files/3.txt', 'r').readlines()))

count = 0

for i in range(len(f) - 3):
    s = f[i] + f[i + 1] + f[i + 2] + f[i + 3]
    if (f[i] % 2 != 0
            and f[i + 1] % 2 != 0
            and f[i + 2] % 2 != 0
            and f[i + 3] % 2 != 0
            and '888' in str(s)):
        count += 1

print(count)
