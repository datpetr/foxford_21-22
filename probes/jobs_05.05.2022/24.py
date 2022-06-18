f = open('files/24.txt', 'r').readline()

f = f.replace('AB', '*')
f = f.replace('CB', '*')
f = f.replace('BC', '*')
f = f.replace('BA', '*')

for i in 'ABCDEF':
    f = f.replace(f'{i}', ' ')
print(f)
lengts = [len(i) for i in f.split()]
print(max(lengts))
