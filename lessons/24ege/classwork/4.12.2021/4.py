f = open('files/24_4.txt', 'r').readline()

count = 0
count_length = 1
mx = 0

for i in range(1, len(f) - 4):
    if f[i] >= f[i - 1]:
        count_length += 1
    else:
        if count_length > mx:
            mx = count_length
            count = 1
        elif count_length == mx:
            count += 1
        count_length = 1

if count_length > mx:
    mx = count_length
    count = 1
elif count_length == mx:
    count += 1

print(mx, count)
