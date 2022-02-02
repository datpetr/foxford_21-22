x = 21
y = 13
z = 7
n = 10 ** 20

ans = min(x, y, z) * 2
n = n - 2  # два уже напечатали

left = 0
right = min(x, y, z) * n  # печатая на одном ксероксе, точно за это время справимся

while right > left + 1:
    t = (left + right) // 2
    if t // x + t // y + t // z < n:
        left = t
    else:
        right = t

ans += t
print(ans)
