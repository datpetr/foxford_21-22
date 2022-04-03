f = open('files/24_7.txt', 'r').read().splitlines()

count = 0

for st in f:
    flag = True
    if (st.count('.') != 3 or st.count('..') != 1
            or st[-1] == '.' or st[0] == '.'):
        flag = False
    else:
        a, b, c, d = map(int, st.split('.'))
        if (not(1 < a < 255)) or (not(1 < b < 255)) or (not(1 < c < 255)) or (not(1 < d < 255)):
            flag = False
    if not flag:
        count += 1
        print(st)

print(count)
