from itertools import permutations


f = open('files/3.txt', 'r').readline()
list_permutations = list(set(map(''.join, permutations('ABCDE', 4))))
count = 0

print(list_permutations)

for i in list_permutations:
    count += f.count(i)

print(count)
