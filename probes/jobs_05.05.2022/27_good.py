f = open('files/27-A.txt', 'r')

n, k = map(int, f.readline().split())
a = list(map(int, f.readlines()))

count, mn = 0, 10 ** 10
cur_sum = beg_sum = 0
for i in range(n):
    cur_sum += a[i]
    count += 1
    if cur_sum - beg_sum == k and count < mn:
        mn = count
        beg_sum += cur_sum
        cur_sum = count = 0
    else:
        if cur_sum - beg_sum > k:
            beg_sum += cur_sum
            cur_sum = count = 0

print(mn)
