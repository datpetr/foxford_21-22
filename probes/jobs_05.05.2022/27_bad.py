f = open('files/27-A.txt', 'r')

n, k = map(int, f.readline().split())
a = list(map(int, f.readlines()))

f.close()

mn = 10 ** 10
for i in range(n - 1):
    sum_of_liters = a[i]
    amount = 1
    for j in range(i + 1, n):
        sum_of_liters += a[j]
        amount += 1
        if sum_of_liters == k:
            if amount < mn:
                mn = amount
            break
        if sum_of_liters > k:
            break

print(mn)
