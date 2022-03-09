f = open('files/3b.txt', 'r')

n = int(f.readline())

pairs = []
count = 0
min_ = [10001] * 8

for _ in range(n):
    k = list(map(int, f.readline().split()))
    k.sort(reverse=True)
    pairs.append(k)


for i in pairs:
    count += i[0]
    s01 = i[0] - i[1]
    s02 = i[0] - i[2]
    if s01 % 8 in range(1, 8) and s01 < min_[s01 % 8]:
        min_[s01 % 8] = s01
    if s02 % 8 in range(1, 8) and s02 < min_[s02 % 8]:
        min_[s02 % 8] = s02

print(count, min_)
