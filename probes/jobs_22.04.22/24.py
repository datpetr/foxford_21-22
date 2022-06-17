f = open('files/24.txt', 'r').readline()

mx = 0
for j in range(2):
    length = 0
    for i in range(j, len(f) - 1, 2):
        if f[i] + f[i + 1] == 'AA' or f[i] + f[i + 1] == 'CC':
            length += 1
            mx = max(mx, length)
        else:
            length = 0

print(mx)
