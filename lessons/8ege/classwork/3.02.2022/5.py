count = 0

for a1 in 'солвей':
    for a2 in 'солвей':
        for a3 in 'солвей':
            for a4 in 'солвей':
                for a5 in 'солвей':
                    for a6 in 'солвей':
                        st = a1 + a2 + a3 + a4 + a5 + a6
                        if (st.count('й') <= 1 and a1 != 'й'
                                and a6 != 'й' and st.count('ей') == 0 and
                                st.count('йе') == 0):
                            count += 1

print(count)
