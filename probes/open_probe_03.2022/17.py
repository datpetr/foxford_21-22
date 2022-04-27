f = list(map(int, open('files/17.txt', 'r').readlines()))

sr_ar = sum(f) / len(f)
count = 0
mx_pair = 0

for i in range(len(f) - 1):
    pair = f[i] + f[i + 1]
    if pair < sr_ar and (str((f[i]))[-1] == '9' or str((f[i + 1]))[-1] == '9'):
        count += 1
        if pair > mx_pair:
            mx_pair = pair

print(count, mx_pair)

