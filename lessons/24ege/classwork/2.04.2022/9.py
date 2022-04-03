f = open('files/24_9.txt', 'r').readline().strip().split('.')

mx = 0

for i in f:
    if i.count('A') >= 3 and len(i) > mx:
        mx = len(i)

print(mx)