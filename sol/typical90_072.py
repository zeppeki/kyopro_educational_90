H, W = map(int, input().split())

C = [input() for _ in range(H)]

used = [[False] * W for _ in range(H)]
dist = [[-1] * W for _ in range(H)]

def dfs(i, j, d):
    used[i][j] = True

    n = dist[i][j]
    if n != -1:
        if d - n < 3:
            return -1
        return d - n
    
    dist[i][j] = d
    ret = -1
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        xi, xj = i + di, j + dj
        if xi < 0 or xi >= H or xj < 0 or xj >= W or C[i][j] == "#":
            continue
        ret = max(ret, dfs(xi, xj, d+1))
    dist[i][j] = -1
    return ret

ans = -1
for i in range(H):
    for j in range(W):
        if used[i][j] or C[i][j] == "#":
            continue
        ans = max(ans, dfs(i, j, 0))
print(ans)
