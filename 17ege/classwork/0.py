f = list(map(int, open('files/17_1.txt', 'r').readlines()))

count = 0
mx_el = 0
mx_answer = 0

for i in f:
    if i % 3 == 0 and i > mx_el:
        mx_el = i

for i in range(len(f) - 1):
    if (f[i] % 3 == 0 or f[i + 1] % 3 == 0) and (f[i] + f[i + 1] <= mx_el):
        count += 1
        if mx_answer < f[i] + f[i + 1]:
            mx_answer = f[i] + f[i + 1]


print(count, mx_answer, mx_el)
