f = list(map(int, open('files/17_4.txt', 'r').readlines()))

count = 0
mx = 0
sr_meaning_f = sum(f) // len(f)

for i in range(len(f) - 2):
    if f[i] < sr_meaning_f or f[i + 1] < sr_meaning_f or f[i + 2] < sr_meaning_f:
        if '8' in str(f[i]) or '8' in str(f[i + 1]) or '8' in str(f[i + 2]):
            count += 1
            if mx < f[i] + f[i + 1] + f[i + 2]:
                mx = f[i] + f[i + 1] + f[i + 2]

print(count, mx)
