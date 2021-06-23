N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            for d in range(c+1,N):
                for e in range(d+1,N):
                    v = (((A[a] * A[b] % P) * A[c] % P) * A[d] % P) * A[e]
                    if v % P == Q:
                        ans += 1
print(ans)
