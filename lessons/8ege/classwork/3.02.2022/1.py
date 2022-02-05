k = 0

for a1 in 'крыша':
    for a2 in 'крыша':
        for a3 in 'крыша':
            for a4 in 'крыша':
                for a5 in 'крыша':
                    st = a1 + a2 + a3 + a4 + a5
                    if (st.count('к') == st.count('р') == st.count('ш') == 0
                            and st.count('ы') <= 2) and st.count('а') <= 2:
                        k += 1

print(k)
