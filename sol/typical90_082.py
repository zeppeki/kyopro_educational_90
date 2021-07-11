L, R = map(int, input().split())

sL = len(str(L))
sR = len(str(R))

ans = 0
for s in range(sL, sR+1):
    x = max(10 ** (s-1), L)
    y = min(10 ** s - 1, R)
    n = y * (y+1) // 2 - x * (x-1) // 2
    ans += n * s
    ans %= 10**9 + 7
print(ans)
