f = open('files/24.txt', 'r').readline().strip()

for i in 'BCDEF':
    f = f.replace('A{}'.format(i), '*')

f = f.replace('A', '*')

for i in 'BCDEF':
    f = f.replace(i, ' ')

lengts = [len(i) for i in f.split()]
print(max(lengts) + 1)