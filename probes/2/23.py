n = 22

dp = [0] * (n + 1)
dp[5] = 1

for i in range(5, 12):
    if i >= 1 and i >= 3 and i >= 4:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4] + 1
    if i >= 1 and i >= 3:
        dp[i] = dp[i - 1] + dp[i - 3] + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp)

for i in range(11):
    dp[i] = 0

print(dp)

for i in range(12, n + 1):
    if i == 14:
        dp[i] = 0
    elif i >= 1 and i >= 3 and i >= 4:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4] + 1
    elif i >= 1 and i >= 3:
        dp[i] = dp[i - 1] + dp[i - 3] + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp)
