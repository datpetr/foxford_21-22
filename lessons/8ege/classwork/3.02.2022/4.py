count = 0

for a1 in 'сакур':
    for a2 in 'сакур':
        for a3 in 'сакур':
            for a4 in 'сакур':
                for a5 in 'сакур':
                    st = a1 + a2 + a3 + a4 + a5
                    if st.count('a') <= 1 and st.count('y') <= 1:
                        count += 1

print(count)
