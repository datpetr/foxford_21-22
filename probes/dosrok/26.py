f = open('files/26.txt', 'r')

n = int(f.readline())
pairs = []
count = 0
mx_r = 0
mn_place = 0

for _ in range(n):
    pairs.append(list(map(int, f.readline().split())))

pairs.sort(key=lambda x: (x[0], -x[1]))

for i in range(n - 1):
    if pairs[i][0] == pairs[i + 1][0]:
        if pairs[i][1] - pairs[i + 1][1] - 1 == 11:
            mx_r = pairs[i][0]
            mn_place = pairs[i + 1][1]
    else:
        count = 0

print(mx_r, mn_place + 1)
