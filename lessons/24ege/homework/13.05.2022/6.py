f = open('files/6.txt', 'r').readline()

a = [0]
mx = 0

for i in range(len(f)):
    if f[i] == 'F':
        a.append(i)

for i in range(len(a) - 4):
    length = a[i + 4] - a[i] - 1
    if length > mx:
        mx = length

print(mx)
