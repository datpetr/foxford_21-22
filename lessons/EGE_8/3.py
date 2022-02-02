count = 0

for a1 in "ЭТАН":
    for a2 in "ЭТАН":
        for a3 in "ЭТАН":
            for a4 in "ЭТАН":
                for a5 in 'ЭТАН':
                    st = a1 + a2 + a3 + a4 + a5
                    if st.count('Э') + st.count('А') == 1:
                        count += 1

print(count)
