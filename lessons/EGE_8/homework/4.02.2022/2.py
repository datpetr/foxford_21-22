count = 0

for a1 in 'ВЫИГРЫВАТЬ':
    for a2 in 'ВЫИГРЫВАТЬ':
        for a3 in 'ВЫИГРЫВАТЬ':
            for a4 in 'ВЫИГРЫВАТЬ':
                for a5 in 'ВЫИГРЫВАТЬ':
                    for a6 in 'ВЫИГРЫВАТЬ':
                        for a7 in 'ВЫИГРЫВАТЬ':
                            for a8 in 'ВЫИГРЫВАТЬ':
                                for a9 in 'ВЫИГРЫВАТЬ':
                                    for a10 in 'ВЫИГРЫВАТЬ':
                                        st = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
                                        
                                        if a1 != 'Ь':
                                            flag = True
                                            for i in range(9):
                                                if st[i] in 'ЫИА' and st[i + 1] in 'ЫИА':
                                                    flag = False
                                                    break

                                            if flag:
                                                print(count)
                                                count += 1

print(count)
буквы