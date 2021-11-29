f = open('name_of_file').readlines()
k = list(map(int, f))

max_k = 0
count = 0

for i in range(len(k) - 1):
    for j in range(i + 1, len(k)):
        s = k[i] + k[j]
        if k[i] > k[j] and s % 3 == 0 and s in k:
            count += 1
            if s > max_k:
                max_k = k[i]

print(max_k, count)
