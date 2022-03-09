f = open('files/4a.txt', 'r')

n = int(f.readline())

pairs = []
count = 0
min_ = [10001] * 11

for _ in range(n):
    k = list(map(int, f.readline().split()))
    k.sort(reverse=True)
    pairs.append(k)


for i in pairs:
    count += i[2]
    s01 = i[1] - i[2]
    s02 = i[0] - i[2]
    if s01 % 11 in range(1, 11) and s01 < min_[s01 % 11]:
        min_[s01 % 11] = s01
    if s02 % 11 in range(1, 11) and s02 < min_[s02 % 11]:
        min_[s02 % 11] = s02

print(count, min_)
