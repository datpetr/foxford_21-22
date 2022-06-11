from fnmatch import fnmatch

gen = ((x, sum(map(int, str(x))))
       for x in range(700_000, 1_000_000)
       if x % 13 == 0 for s in str(x,)
       if not any([fnmatch(s, '*0??3*'),
                   fnmatch(s, '*4??2*'),
                   fnmatch(s, '*1*')]))
for _ in range(5):
    print(*next(gen))
