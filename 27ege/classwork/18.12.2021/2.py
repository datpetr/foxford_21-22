f = open('files/27_2B.txt', 'r').readlines()

n = int(f.pop(0))
k = []
flag = True
s = 0
sum_ = 0

for i in f:
    a, b = map(int, i.split())
    s += max(a, b)
    if abs(a - b) % 5 != 0:
        k.append(abs(a - b))

k.sort()

if s % 5 == 0:
    print(s)
else:
    for i in range(len(k)):
        sum_ = k[i]
        if flag:
            for j in range(i, len(k)):
                sum_ += k[j]
                if (s - sum_) % 5 == 0:
                    print(s - sum_)
                    flag = False
                    break
        else:
            break
