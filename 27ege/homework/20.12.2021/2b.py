f = open('files/2B.txt', 'r')

n = int(f.readline())

sum = 0
mnd = n + 1

for i in range(n):
    a, b = map(int, f.readline().split())
    sum += max(a, b)
    d = abs(a - b)
    if d % 4 != 0:
        mnd = min(d, mnd)

if sum % 4 != 0:
    print(sum)
else:
    print(sum - mnd)
