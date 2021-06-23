K = int(input())

MOD = 10 ** 9 + 7

dp = [0 for _ in range(K+1)]
dp[0] = 1

for i in range(K+1):
    x = min(i, 9)
    for j in range(1, x+1):
        dp[i] += dp[i-j]
    dp[i] %= MOD

if K % 9 != 0:
    print(0)
else:
    print(dp[-1])
