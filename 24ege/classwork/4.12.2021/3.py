f = open('files/24_3.txt', 'r').readline()

count = 0

for i in range(len(f) - 4):
    if f[i] <= f[i + 1] <= f[i + 2] <= f[i + 3] <= f[i + 4]:
        count += 1
        ans = i + 1


print(count, ans)
