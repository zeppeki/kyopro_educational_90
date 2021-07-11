N, Q = map(int, input().split())

P = []
INF = 10 ** 10
xmin, xmax = INF, -INF
ymin, ymax = INF, -INF

for _ in range(N):
    x, y = map(int, input().split())
    P.append((x-y, x+y))
    xmin = min(xmin, x-y)
    xmax = max(xmax, x-y)
    ymin = min(ymin, x+y)
    ymax = max(ymax, x+y)

for _ in range(Q):
    q = int(input())
    qx, qy = P[q-1]
    ans = max(abs(xmax-qx), abs(xmin-qx), abs(ymax-qy), abs(ymin-qy))
    print(ans)
