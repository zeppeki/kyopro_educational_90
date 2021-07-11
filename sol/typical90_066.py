N = int(input())
X = []
for _ in range(N):
    L, R = map(int, input().split())
    X.append((L, R))

ans = 0
for i in range(N):
    Li, Ri = X[i]
    zi = Ri - Li + 1
    for j in range(i+1, N):
        Lj, Rj = X[j]
        zj = Rj - Lj + 1
        v = 0.0
        for x in range(Lj, Rj+1):
            v += min(max(Ri - x, 0), zi)
        a = v / zi / zj
        ans += a
print(ans)
