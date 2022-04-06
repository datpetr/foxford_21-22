f = open('files/1.txt', 'r').readline()

subsequence_signs = ['D', 'A', 'B', 'E']
mx = 0
count = 0
count_sign = 0

for i in range(len(f)):
    if f[i] == subsequence_signs[count_sign % 4]:
        count += 1
        count_sign += 1
    else:
        if mx < count:
            mx = count
        count = count_sign = 0

print(mx)