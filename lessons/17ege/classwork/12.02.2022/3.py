f = list(map(int, open('files/17_3.txt', 'r').readlines()))

average = 0
mx = -10001
count = 0
average = sum(f) / len(f)

for i in range(len(f) - 2):
    flag = True
    first = max(f[i], f[i + 1], f[i + 2])
    third = min(f[i], f[i + 1], f[i + 2])
    second = f[i] + f[i + 1] + f[i + 2] - first - third

    for i in f[i], f[i + 1], f[i + 2]:
        if '1' not in str(i):
            flag = False
            break

    if third < average and second < average and flag:
        count += 1
        if mx < first + second + third:
            mx = first + second + third

print(count, mx)
