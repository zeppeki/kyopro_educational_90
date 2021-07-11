N = int(input())
S = input()

dp = [[0 for _ in range(N)] for _ in range(7)]

MOD = 10 ** 9 + 7
T = "atcoder"
for i, s in enumerate(S):
    for j, t in enumerate(T):
        if s == t:
            if j == 0:
                v = 1
            else:
                v = dp[j-1][i-1]
        else:
            v = 0
        dp[j][i] = (dp[j][i-1] + v) % MOD

print(dp[-1][-1])
