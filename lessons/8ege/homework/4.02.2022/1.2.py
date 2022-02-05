count = 0

for a1 in 'СЧИТАЙ':
    for a2 in 'СЧИТАЙ':
        for a3 in 'СЧИТАЙ':
            for a4 in 'СЧИТАЙ':
                st = a1 + a2 + a3 + a4
                if st.count('А') <= 1:
                    count += 1

print(count)
            