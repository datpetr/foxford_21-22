for a1 in range(2, 30):
    for a2 in range(2, 30):
        for a3 in range(2, 30):
            st = "0" + "1" * a1 + "2" * a2 + "3" * a3

            while ("01" in st) or ("02" in st) or ("03" in st):
                st = st.replace("01", "210", 1)
                st = st.replace("02", "3101", 1)
                st = st.replace("03", "2302", 1)

            n = len(st)
            k1 = 0
            k2 = 0
            k3 = 0

            for i in range(n):
                if int(st[i]) == 1:
                    k1 += 1
                if int(st[i]) == 2:
                    k2 += 1
                if int(st[i]) == 3:
                    k3 += 1

            if k1 == 52 and k2 == 33 and k3 == 23:
                print(a2)
