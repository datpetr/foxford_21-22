print('x y z w  f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x and z) or ((not w or x) == (not z or y))
                if not(f):
                    print(x, y, z, w, int(not(f)))
