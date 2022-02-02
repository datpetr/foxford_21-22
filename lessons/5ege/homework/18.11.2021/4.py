k = []
for i in range(1, 1000):
    s = bin(i)[2:]
    if i % 2 == 0:
        s += '01'
    else:
        s += '10'

    print(int(s, 2))
    k.append(int(int(s, 2)))
print(min(k))
