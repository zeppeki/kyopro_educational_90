N, K = map(int, input().split())

P = 10**9 + 7

if N == 1:
    ans = K
else:
    ans = K * (K - 1)
    ans *= pow(K-2, N-2, mod=P)

ans %= P
print(ans)
