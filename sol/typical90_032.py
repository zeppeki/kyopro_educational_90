import itertools

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

X = [[False for _ in range(N)] for _ in range(N)]
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    X[x-1][y-1] = True
    X[y-1][x-1] = True


INF = 1000000

ans = INF
for x in itertools.permutations(range(N)):
    f = True
    for j in range(N-1):
        if X[x[j]][x[j+1]]:
            f = False
    if f:
        v = 0
        for j, i in enumerate(x):
            v += A[i][j]
        ans = min(ans, v)

if ans == INF:
    print(-1)
else:
    print(ans)
