mn_numb = 10 ** 10
mn_length = 0

for i in range(100, 1001):
    s = '3' * i
    while '111' in s or '333' in s:
        if '111' in s:
            s = s.replace('111', '3', 1)
        else:
            s = s.replace('333', '1', 1)

    if int(s) < mn_numb:
        mn_numb = int(s)
        mn_length = i

print(mn_numb, mn_length)
