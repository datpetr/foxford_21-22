f = open('files/2.txt', 'r').readline()

count = 1
mx = 0
sign = ''

for i in range(len(f) - 1):
    if f[i] == f[i + 1]:
        count += 1
    else:
        if mx < count:
            mx = count
            sign = f[i]
        count = 1

print(mx, sign)
