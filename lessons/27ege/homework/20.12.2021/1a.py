from copy import deepcopy

f = open('files/1A.txt', 'r').readlines()
n = int(f.pop(0))

k = []
k2 = []
k_max = []
k_min = []
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for i in f:
    k.append(list(map(int, i.split())))

k.append([0, 0])
k2 = deepcopy(k)

for i in range(len(k)):
    if k[i][0] > k[i][1]:
        k2[i] = [k[i][0], k[i][1]]
    else:
        k2[i] = [k[i][1], k[i][0]]

for i in range(len(k2) - 1):
    if (k2[i][0] + k2[i + 1][0]) % 2 == 0:
        sum1 = k2[i][0] + k2[i + 1][0]
    elif (k2[i][1] + k2[i + 1][0]) % 2 == 0:
        sum1 = k2[i][1] + k2[i + 1][0]
    elif (k2[i][1] + k2[i + 1][1]) % 2 == 0:
        sum1 = k2[i][1] + k2[i + 1][1]
    elif (k2[i][0] + k2[i + 1][1]) % 2 == 0:
        sum1 = k2[i][0] + k2[i + 1][1]
    k_max.append(max(sum1, sum2, sum3, sum4))
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0

for i in range(len(k2) - 1):
    if (k2[i][0] + k2[i + 1][0]) % 2 == 0:
        sum1 = k2[i][0] + k2[i + 1][0]
    elif (k2[i][1] + k2[i + 1][0]) % 2 == 0:
        sum1 = k2[i][1] + k2[i + 1][0]
    elif (k2[i][1] + k2[i + 1][1]) % 2 == 0:
        sum1 = k2[i][1] + k2[i + 1][1]
    elif (k2[i][0] + k2[i + 1][1]) % 2 == 0:
        sum1 = k2[i][0] + k2[i + 1][1]
    k_min.append(min(sum1, sum2, sum3, sum4))
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0


print(k_max, k_min)
print(sum(k_max) - sum(k_min))