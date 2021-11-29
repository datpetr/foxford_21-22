count = 0

for a1 in "КРОТ":
    for a2 in "КРОТ":
        for a3 in "КРОТ":
            for a4 in "КРОТ":
                for a5 in "КРОТ":
                    for a6 in "КРОТ":
                        st = a1 + a2 + a3 + a4 + a5 + a6
                        if st.count('О') == 1:
                            count += 1

print(count)
