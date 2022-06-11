from itertools import permutations

a = list(map(''.join, (permutations('ГЕПАРД', 5))))

count = 0

for i in a:
    if i.count('Г') == 1 and i[0] != 'A' and i[-1] != 'Е':
        count += 1
        print(i)

print(count)
