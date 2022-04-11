f = open('files/1.txt', 'r')

n, s = map(int, f.readline().split())

a_group = []
b_group = []

count_sum = 0
count_products_b = 0
last = 0

for _ in range(n):
    pair = f.readline().split()
    if pair[-1] == 'A':
        a_group.append(list(map(int, pair[:-1])))
    else:
        b_group.append(list(map(int, pair[:-1])))


for i in a_group:
    count_sum += i[0] * i[1]
    count_products_b += 1

b_group.sort(key=lambda x: x[0])
ind = 0

while s - count_sum >= 0:
    count_sum += b_group[ind][0] * b_group[ind][1]
    ind += 1
    count_products_b += 1
    last = b_group[ind][0] * b_group[ind][1]

print(count_products_b, s - count_sum + last)
