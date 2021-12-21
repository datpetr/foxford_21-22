f = open('filles/2A.txt', 'r')

sum = 0
mnd = 10001

for i in range(7):
    a, b = map(int, f.readline().split())
    sum += max(a, b)
    d = abs(a - b)

    if d % 4 != 0:
        mnd = min(d, mnd)

if sum % 4 != 0:
    print(sum)
else:
    print(sum - mnd)
