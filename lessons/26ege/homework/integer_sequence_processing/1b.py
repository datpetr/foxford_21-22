f = open('files/1b.txt', 'r')

n = int(f.readline())
a = []
mx = 0

for _ in range(n):
    pair = list(map(int, f.readline().split()))
    a.append(pair)

for i in a:
    n1 = i[0]
    n2 = i[1]
    mx += max(n1, n2)

if mx % 4 != 0:
    print(mx)
else:
    print(0)
