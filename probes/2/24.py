f = open('files/24.txt', 'r').readline()

a = [0] * len(f)
length = 0
mx = 0
count = 0
beg = 0

for i in range(len(f)):
    if f[i] == 'F':
        a[i] = 1

for i, val in enumerate(a):
    if val == 1:
        count += 1
        while count < 3:
            if val == 1:
                count += 1
            else:
