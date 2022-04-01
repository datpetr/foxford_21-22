f = open('files/1b.txt', 'r')

n = int(f.readline())
mn = [100000 + 1] * 5
sum_elems = 0

for _ in range(n):
    a, b, c = list(map(int, f.readline().split()))
    sum_elems += max(a, b, c)
    for i in a, b, c:
        if i < mn[i % 5]:
            mn[i % 5] = i


print(sum_elems, mn)
