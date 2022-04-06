f = open('files/2b.txt', 'r')

n = int(f.readline())
count_even = 0
count_odd = 0
mn_odd = 100001
s = 0

for i in range(n):
    d = list(map(int, f.readline().split()))
    d.sort(reverse=True)
    s += d[0]

    if d[0] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

    if (d[0] - d[1]) % 2 != 0:
        if d[0] - d[1] < mn_odd:
            mn_odd = d[0] - d[1]

if count_odd > count_even:
    if s % 2 != 0:
        print(s)
    else:
        print(s - mn_odd)
else:
    if s % 2 == 0:
        print(s)
    else:
        print(s - mn_odd)
