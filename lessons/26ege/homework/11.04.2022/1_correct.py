with open("files/1.txt") as F:
    N, S = map(int, F.readline().split())

    data = []
    for i in range(N):
        price, size, model = F.readline().split()
        data.append((int(price), int(size), model))

data.sort(key=lambda d: (d[2], d[0]))

xSum = 0
countZ = 0

for d in data:
    if xSum + d[0] > S:
        break
    thisCount = min(d[1], (S - xSum) // d[0])
    xSum += d[0] * thisCount
    if d[2] == 'B':
        countZ += thisCount

print(countZ, S - xSum)
