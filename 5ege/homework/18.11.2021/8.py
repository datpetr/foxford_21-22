s = '>' + '1' * 20 + '2' * 20 + '3' * 10
while '>1' in s or '>2' in s or '>3' in s:
    s = s.replace('>1', '22>3', 1)
    s = s.replace('>2', '33>', 1)
    s = s.replace('>3', '11>2', 1)

print(s.count('1') + s.count('2') * 2 + s.count('3') * 3)
