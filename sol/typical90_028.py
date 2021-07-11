N = int(input())

V = [[0 for _ in range(1001)] for _ in range(1001)]
U = [[0 for _ in range(1001)] for _ in range(1001)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    V[lx][ly] += 1
    V[rx][ly] -= 1
    V[lx][ry] -= 1
    V[rx][ry] += 1

for x in range(1001):
    v = 0
    for y in range(1001):
        v += V[x][y]
        U[x][y] = v

ans = [0 for _ in range(N+1)]
for y in range(1001):
    u = 0
    for x in range(1001):
        u += U[x][y]
        ans[u] += 1

for i in range(1, N+1):
    print(ans[i])
