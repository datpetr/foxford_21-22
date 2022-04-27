mx = 0
length = 0
length_beg = 0

for i in range(300, 1000):
    s = '5' * i
    length_beg = len(s)
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    print(s.count('5'))
    if mx < s.count('5'):
        length = length_beg
        mx = s.count('5')


print(length)
