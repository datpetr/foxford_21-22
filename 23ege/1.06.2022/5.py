n = 89

dp = [0] * (n + 1)

for i in range(4, n + 1):
    if (i // 2) * 2 == i and (i // 3) * 3 == i:
        dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3]) + 1
    elif (i // 2) * 2 == i:
        dp[i] = min(dp[i - 1], dp[i // 2]) + 1
    elif (i // 3) * 3 == i:
        dp[i] = min(dp[i - 1], dp[i // 3]) + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp)
