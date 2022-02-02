for a1 in range(1, 100):
    for a2 in range(1, 100):
        for a3 in range(1, 100):
            s = '0' + '1' * a1 + '2' * a2 + '3' * a3
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2302', 1)
            if s.count('1') == 52 and s.count('2') == 33 and s.count('3') == 23:
                print(a2)
