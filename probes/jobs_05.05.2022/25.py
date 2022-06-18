def f(numb):
    n = str(numb)
    prev_number = n[0]
    for i in range(1, len(n)):
        if not(n[i] > prev_number):
            return False
        else:
            prev_number = n[i]
    return True


n = 103
amount_answers = 0
while amount_answers < 4:
    if f(n) and n % 103 == 0:
        print(n, n // 103)
        amount_answers += 1
    n += 103
