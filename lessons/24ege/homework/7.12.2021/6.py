f = open('files/24-1.txt', 'r').readline()

s = ''
mx = 0
k = []

for i in f:
    if i in '0123456789':
        s += i
    else:
        if s != '':
            k.append(s)
            s = ''

k = list(map(int, k))

for i in k:
    if i % 2 == 0 and i > mx:
        mx = i

print(mx)
