n = 36
dp = [0] * (n + 1)

dp[10] = 1

for i in range(11, 18):
    if (i // 2) * 2 == i:
        dp[i] = dp[i // 2] + dp[i - 2] + dp[i - 3]
    else:
        dp[i] = dp[i - 2] + dp[i - 3]

print(dp)

for i in range(17):
    dp[i] = 0

print(dp)

for i in range(19, n + 1):
    if (i // 2) * 2 == i:
        dp[i] = dp[i // 2] + dp[i - 2] + dp[i - 3]
    else:
        dp[i] = dp[i - 2] + dp[i - 3]

print(dp)
