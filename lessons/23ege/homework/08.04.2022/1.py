n = 36

dp = [0] * (n + 1)
dp[10] = 1

for i in range(11, 18):
    if (i // 2) * 2 == i and i > 3 and i > 2:
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i // 2] + 1
    elif (i // 3) * 3 == i and i > 3:
        dp[i] = dp[i - 3] + dp[i // 2] + 1
    elif (i // 2) * 2 == i and i > 2:
        dp[i] = dp[i - 2] + dp[i // 2] + 1
    elif (i // 2) * 2:
        dp[i] = dp[i // 2] + 1
    elif i > 3:
        dp[i] = dp[i - 3] + 1
    elif i > 2:
        dp[i] = dp[i - 2] + 1

print(dp)

for i in range(17):
    dp[i] = 0

print(dp)

