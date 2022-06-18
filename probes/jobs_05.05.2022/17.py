from collections import Counter

f = list(map(int, open('files/17.txt', 'r').readlines()))

count = 0
a = []

for i in range(1, len(f) - 1):
    sum_index_prev = sum([int(x) for x in str(abs(f[i - 1]))])
    sum_index_following = sum([int(x) for x in str(abs(f[i + 1]))])
    if sum_index_prev == sum_index_following:
        count += 1
        a.append(sum(map(int, str(f[i]))))

print(count, Counter(a).most_common()[0][0])
