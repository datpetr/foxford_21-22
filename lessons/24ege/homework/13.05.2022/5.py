f = open('files/5.txt', 'r').readline()

count = 1
mx = 0

for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        count += 1
        if mx < count:
            mx = count
    else:
        count = 1

print(mx)