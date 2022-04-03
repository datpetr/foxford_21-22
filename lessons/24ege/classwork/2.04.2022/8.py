f = open('files/24_8.txt', 'r').readline()

mx = 0
count = 1
for i in range(len(f) - 1):
    if (f[i] + f[i + 1]) not in ['PR', 'RP']:
        count += 1
        if count > mx:
            mx = count
    else:
        count = 1

print(mx)
