f = open('files/24.txt').readline()

while 'CACAC' in f:
    f = f.replace('CACAC', 'CAC CAC')

f = f.replace('CAC', '***').replace('AB', '**')
f = f.replace('A', ' ').replace('B', ' ').replace('C', ' ')

lengths = [len(i) for i in f.split()]

print(max(lengths))
