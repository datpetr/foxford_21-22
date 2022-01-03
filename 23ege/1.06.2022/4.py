st = set()


def nProg(x, t):
    if t == 13:
        st.add(x)
    elif t < 13:
        nProg(x + 3, t + 1)
        nProg(x * 2 + 1, t + 1)


nProg(2, 0)
print(len(st))
