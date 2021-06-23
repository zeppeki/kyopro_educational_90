N, Q = map(int, input().split())
A = list(map(int, input().split()))

D = [A[i+1] - A[i] for i in range(N-1)] 
ans = 0
for v in D:
    ans += abs(v)

for _ in range(Q):
    L, R, V = map(int, input().split())
    L -= 1
    R -= 1
    if L > 0:
        u = D[L-1]
        ans += abs(u + V) - abs(u)
        D[L-1] += V
    if R < N-1:
        u = D[R]
        ans += abs(u - V) - abs(u)
        D[R] -= V

    print(ans)
