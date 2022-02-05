count = 0
vowels = 'АИЕ'
consonants = 'ЗДН'


for a1 in 'ЗДАНИЕ':
    for a2 in 'ЗДАНИЕ':
        for a3 in 'ЗДАНИЕ':
            for a4 in 'ЗДАНИЕ':
                for a5 in 'ЗДАНИЕ':
                    for a6 in 'ЗДАНИЕ':
                        st = a1 + a2 + a3 + a4 + a5 + a6
                        if ((((a1 and a3 and a5) in vowels) and (a2 and a4 and a6) in consonants)
                            or (((a1 and a3 and a5) in consonants) and (a2 and a4 and a6) in vowels)) \
                                and (st.count('З') == 1 and
                                st.count('Д') == 1 and
                                st.count('А') == 1 and
                                st.count('Н') == 1 and
                                st.count('И') == 1 and
                                st.count('Е') == 1):
                            count += 1

print(count)
