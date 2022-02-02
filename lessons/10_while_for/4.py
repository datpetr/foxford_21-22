k = []


for i in range(333666, 666999 + 1):
    if str(i).count('7') >= 2 and i % 17 == 0:
        k.append(i)


print(len(k), max(k))
print(k)