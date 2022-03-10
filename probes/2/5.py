def func(n):
    st_2 = bin(n)[2:]

    if int(st_2) % 2 == 0:
        st_2 += '01'
    else:
        st_2 += '10'

    count = 0

    for i in st_2:
        count += int(i)

    st_2 += str(count % 2)
    return st_2


for i in range(1, 1000):
    n = int(int(func(i), 2))
    if n > 147 and len(func(i)) > len(bin(i)[2:]):
        print(n)
        break
