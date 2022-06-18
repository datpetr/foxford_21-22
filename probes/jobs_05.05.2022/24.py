
f = open('files/24.txt', 'r').readline().strip()

combinations_of_letters = ['AB', 'CB', 'BC', 'BA']

mx = count = 0

for i in range(len(f) - 1):
    if f[i:i + 2] in combinations_of_letters:
        count += 1
    else:
        count = 0

    mx = max(mx, count)

print(mx)
# f = open('files/24.txt', 'r').readline()
#
# f = f.replace('AB', '*')
# f = f.replace('CB', '*')
# f = f.replace('BC', '*')
# f = f.replace('BA', '*')
#
# for i in 'ABCDEF':
#     f = f.replace(f'{i}', ' ')
# print(f)
# lengts = [len(i) for i in f.split()]
# print(max(lengts))

