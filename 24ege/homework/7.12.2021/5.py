f = open('files/24-164.txt', 'r').readlines()

count = 1
count_sign = 0
mx = 0
mn = 100000000000
s = ''

for i in f:
    for j in range(len(i)):
        if i[j - 1] == i[j]:
            count += 1
            if count > mx:
                mx = count
                s = i
        else:
            count = 1

sign = s[0]

for i in s:
    if s.count(i) < mn and ord(i) > ord(sign):
        sign = i
        mn = s.count(i)

for i in f:
    count_sign += i.count(sign)

print('{}{}'.format(sign, count_sign))
