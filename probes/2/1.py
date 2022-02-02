print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                condition = ((x == (not w)) <= (z and (not x))) or ((y and w) and z)
                if not condition:
                    print(x, y, z, w)
