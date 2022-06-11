print('a b c d f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = (d and ((not (a or (not c))) or a and b and (not c)))
                if f:
                    print(a, b, c, d, f)
