f = open('files/file.txt').readlines()

count = 0
for i in f:
    if i.count('K') > i.count('U'):
        count += 1

print(count)
