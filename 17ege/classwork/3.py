f = list(map(int, open('files/17_3.txt', 'r').readlines()))

count = 0
min_ = max(f)
sr_meaning_f = sum(f) // len(f)

for i in range(len(f) - 1):
    if (f[i] > sr_meaning_f or f[i + 1] > sr_meaning_f) and ((f[i] + f[i + 1]) % 7 == 0):
        count += 1
        if min_ > (f[i] + f[i + 1]):
            min_ = (f[i] + f[i + 1])

print(count, min_)
