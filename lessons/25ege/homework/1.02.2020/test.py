def alogoritm(n):
    st_2 = bin(n)[2:]

    for _ in range(2):
        st_2 += str(st_2.count('1') % 2)

    return st_2


for i in range(1, 10000):
    s = alogoritm(i)
    if len(s) - len(bin(i)[2:]) == 2:
        if int(int(s, 2)) > 63:
            print(int(s, 2))
            break
