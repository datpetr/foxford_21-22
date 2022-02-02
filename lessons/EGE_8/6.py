count = 0
flag = True

for val1 in 'КОСФ':
    for val2 in 'КОСФ':
        for val3 in 'КОСФ':
            for val4 in 'КОСФ':
                st = val1 + val2 + val3 + val4
                if st == 'ФОКС':
                    print(count + 1)
                    flag = False
                if flag:
                    count += 1
