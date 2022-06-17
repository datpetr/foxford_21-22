from fnmatch import fnmatch


def f(x):
    prev = int(str(x)[0])
    for i in range(1, len(str(x))):
        if not(int(str(x)[i]) > prev):
            return False
        else:
            prev = int(str(x)[i])
    return True


amount_answers = 0
for x in range(159, 159999999):
    if x % 21 == 0 and f(x) and fnmatch(str(x), '1*5*9'):
        print(x, x // 21)
        amount_answers += 1
        if amount_answers == 5:
            break
