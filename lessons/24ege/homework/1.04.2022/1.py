f = open('files/1.txt', 'r').readline()
print(len(f))
subsequence_sign = ['D', 'A', 'B', 'E']
count = 0
count_sign = 0
mx = 0

for i in f:
    if i == subsequence_sign[count_sign % 4]:
        count_sign += 1
        count += 1
    else:
        if mx < count:
            mx = count
        count_sign = 0
        count = 0

print(mx)
