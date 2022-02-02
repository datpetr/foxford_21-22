f = list(map(int, open('files/27_3A.txt').readlines()))
n = f.pop(0)

mx = 0
count_mx = 0

for i in range(n):
    sum_ = 0
    count = 0
    for j in range(i, n):
        sum_ += f[j]
        count += 1
        if sum_ % 100 == 0 and sum_ > mx:
            mx = sum_
            count_mx = count
        elif sum_ == mx:
            if count < count_mx:
                count_mx = count


print(count_mx, mx)
