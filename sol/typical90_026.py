import sys
sys.setrecursionlimit(10**7)

N = int(input())
E = [list() for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)

color = [0 for _ in range(N)]

def dfs(v, c):
    color[v] = c
    for u in E[v]:
        if color[u] == c:
            return False
        if color[u] == 0 and not dfs(u, -c):
            return False
    return True

dfs(0, 1)
if color.count(1) >= N // 2:
    c = 1
else:
    c = -1

ans = []
for i in range(N):
    if color[i] == c:
        ans.append(i+1)
print(*ans[:N//2])
