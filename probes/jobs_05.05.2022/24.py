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
