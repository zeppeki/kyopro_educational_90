import bisect

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

M = N//2

L = [[] for _ in range(N+1)]
R = [[] for _ in range(N+1)]

for i in range(1 << M):
    v, c = 0, 0
    for j in range(M):
        if i & (1 << j):
            v += A[j]
            c += 1
    L[c].append(v)

for i in range(1 << (N - M)):
    v, c = 0, 0
    for j in range(N - M):
        if i & (1 << j):
            v += A[M + j]
            c += 1
    R[c].append(v)


ans = 0
for i in range(M+1):
    L[i].sort()
    R[i].sort()

for k in range(M+1):
    for v in L[k]:
        if P - v >= 0:
            p = bisect.bisect_right(R[K-k], P - v)
            ans += p

print(ans)
