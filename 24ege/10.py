f = open('files/10.txt').readlines()

mx = 0
for i in f:
    if i.count('X') == i.count('Y') == i.count('Z') == 0:
        if i.count('A') > mx:
            mx = i.count('A')

print(mx)
