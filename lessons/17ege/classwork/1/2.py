f = list(map(int, open('files/17_2.txt', 'r').readlines()))

count = 0
mx_answer = 0

for i in range(len(f) - 1):
    if (f[i] % 2 != 0 and f[i + 1] % 2 != 0) \
            and ((f[i] + f[i + 1]) // 2 in f):
        count += 1
        if mx_answer < (f[i] + f[i + 1]) // 2:
            mx_answer = (f[i] + f[i + 1]) // 2


print(count, mx_answer)
