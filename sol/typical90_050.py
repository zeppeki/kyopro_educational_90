N, L = map(int, input().split())

dp = [1]
for n in range(1, N+1):
    if n - L < 0:
        v = dp[n-1]
    else:
        v = dp[n-1] + dp[n-L]
    v %= 10 ** 9 + 7
    dp.append(v)
print(dp[-1])
