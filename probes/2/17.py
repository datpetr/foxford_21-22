numbers = list(map(int, open('files/17.txt', 'r').readlines()))

mx = 0
count = 0

for i in range(len(numbers) - 1):
    pair = numbers[i] + numbers[i + 1]
    if pair % 3 == 0 and pair % 6 != 0:
        if mx < pair:
            mx = pair
        count += 1

print(count, mx)