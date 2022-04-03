from itertools import permutations


f = open('files/3.txt', 'r').readline()

count = 0
lots_of_permutations = list(map(''.join, permutations('ABCDE', 4)))

for i in lots_of_permutations:
    count += f.count(i)

print(count)
