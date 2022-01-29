f = open('files/1a.txt', 'r')

n = 7
a = []
mx = []
count = 0

for _ in range(n):
    pair = list(map(int, f.readline().split()))
    a.append(pair)

for i in range(len(a)):
    count = 0
    for j in range(len(a[i])):
        count += a[i][j]

    pass
