print('x y z w f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x and y) <= (z and w)) and (((not y) and z) == ((not z) or w))
                if f:
                    print(x, y, z, w, f)