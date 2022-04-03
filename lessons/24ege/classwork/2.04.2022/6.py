f = open('files/24_6.txt', 'r').read().splitlines()

sign = ''
st = ''
mx = 0
length = 1
a = [0] * 100
mn = 10 ** 6
count = 0

for i in f:
    for j in range(len(i) - 1):
        if i[j] == i[j + 1]:
            length += 1
            if mx < length:
                mx = length
                st = i
        else:
            length = 1


for i in range(len(st)):
    a[ord(st[i])] += 1

for i in range(len(a)):
    if a[i] != 0 and a[i] < mn:
        mn = a[i]
        ind = i

for i in f:
    count += i.count(chr(ind))

print(a)
print(count, chr(ind))
