for x in range(1, 300):
    for y in range(1, 300):
        for z in range(1, 300):
            st = '1' * x + '2' * y + '3' * z
            while '01' in st or '02' in st or '03' in st:
                st = st.replace('01', '310', 1)
                st = st.replace('02', '1201', 1)
                st = st.replace('03', '3022', 1)
            if st.count('1') == 59 and st.count('2') == 25 and st.count('3') == 42:
                print(x)
                exit(0)
