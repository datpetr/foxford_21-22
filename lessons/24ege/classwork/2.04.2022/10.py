f = open('files/24_10.txt', 'r').readline().strip().split('Y')

mx = 0

for i in f:
    if i.count('.') <= 5 and mx < len(i):
        mx = len(i)
    else:
        dot = [-1]
        for j in range(len(i)):
            if i[j] == '.':
                dot.append(j)
        dot.append(len(i))
        for j in range(len(dot) - 6):
            if dot[j + 6] - dot[j] - 1 > mx:
                mx = dot[j + 6] - dot[j] - 1

print(mx)
