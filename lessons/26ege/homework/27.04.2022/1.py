f = open('files/1.txt', 'r')

n, s = list(map(int, f.readline().split()))
data = []
s_ab = count = 0

for i in range(n):
    a, b, c = f.readline().split()
    data.append([int(a), int(b), str(c)])

f.close()

data.sort(key=lambda x: (x[2], x[0]))

xSum = countZ = 0

for d in data:
    if xSum + d[0] > s:
        break
    thisCount = min(d[1], int((s - xSum) / d[0]))
    xSum += d[0] * thisCount
    if d[2] == 'B':
        countZ += thisCount

print(countZ, s - xSum)
