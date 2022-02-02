st = '2' * 124 + '1' * 19

while '222' in st or '111' in st:
    if '222' in st:
        st = st.replace('222', '1', 1)
    if '111' in st:
        st = st.replace('111', '2', 1)

print(st)