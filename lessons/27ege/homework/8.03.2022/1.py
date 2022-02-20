f = open('files/1b.txt', 'r')

n = int(f.readline())
sum_ = 0
mn = 100001

for _ in range(n):
    pairs = list(map(int, f.readline().split()))
    pairs.sort(reverse=True)
    sum_ += pairs[0]
    if ((abs(pairs[0] - pairs[1])) % 5 != 0) and (abs(pairs[0] - pairs[1]) < mn):
        mn = abs(pairs[0] - pairs[1])
    if ((abs(pairs[0] - pairs[2])) % 5 != 0) and (abs(pairs[0] - pairs[2]) < mn):
        mn = abs(pairs[0] - pairs[2])

if sum_ % 5 != 0:
    print(sum_)
else:
    print(sum_ - mn)

f.close()
