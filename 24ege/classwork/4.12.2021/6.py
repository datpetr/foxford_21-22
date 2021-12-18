f = open('24_6.txt', 'r').readline()

count = 0
s = ''
mx = 0

for i in range(len(f)):
    if f[i] in '0123456789':
        s += f[i]
        if int(s) % 2 != 0:
            mx = int(s)
    else:
        s = ''

print(mx)