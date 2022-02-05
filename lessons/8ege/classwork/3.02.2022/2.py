k = 0

for a1 in 'корнет':
    for a2 in 'корнет':
        for a3 in 'корнет':
            for a4 in 'корнет':
                for a5 in 'корнет':
                    st = a1 + a2 + a3 + a4 + a5
                    if st.count('о') <= 1 and st.count('е') <= 1:
                        k += 1

print(k)
