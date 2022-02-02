count = 0
flag = True

for val1 in 'АИКР':
    for val2 in 'АИКР':
        for val3 in 'АИКР':
            for val4 in 'АИКР':
                for val5 in 'АИКР':
                    st = val1 + val2 + val3 + val4 + val5
                    if st == 'АКИРИ':
                        print(count + 1)
                        flag = False
                    if flag:
                        count += 1
