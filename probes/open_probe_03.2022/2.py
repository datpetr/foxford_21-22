print('x y z w f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = ((y <= z) and (not (z and x)))
            if f:
                print(x, y, z, f)