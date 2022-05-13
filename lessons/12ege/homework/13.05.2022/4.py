s = '>' + '1' * 30 + '2' * 10 + '3' * 20
count = 0

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)

    if '>2' in s:
        s = s.replace('>2', '2>', 1)

    if '>3' in s:
        s = s.replace('>3', '1>', 1)

print(s[:-1])
print(s)
for i in s[:-1]:
    count += int(i)
print(count)