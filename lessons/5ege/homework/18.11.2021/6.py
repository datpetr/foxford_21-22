s = '1' * 2020 + '2' * 2020
while '11111' in s:
    s = s.replace('222', '1', 1)
    s = s.replace('111', '2', 1)

print(s)
