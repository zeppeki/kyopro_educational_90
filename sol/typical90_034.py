N, K = map(int, input().split())
A = list(map(int, input().split()))

d = dict()
r = 0
ans = 0

for i in range(N):
    while r < N and len(d) <= K:
        ans = max(ans, r-i)
        ch = A[r]
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
        r += 1
    if len(d) <= K:
        ans = max(ans, r-i)
    ch = A[i]
    if d[ch] == 1:
        d.pop(ch)
    else:
        d[ch] -= 1
print(ans)
