n = 34

dp = [0] * (n + 1)
dp[4] = 1

for i in range(5, 11):
    if (i // 2) * 2 == i and (i // 3) * 3 == i:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif (i // 2) * 2 == i:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif (i // 3) * 3 == i:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]

print(dp)

for i in range(10):
    dp[i] = 0

print(dp)

for i in range(11, n + 1):
    if i == 18:
        dp[i] = 0
    elif (i // 2) * 2 == i and (i // 3) * 3 == i:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif (i // 2) * 2 == i:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif (i // 3) * 3 == i:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]

print(dp)
