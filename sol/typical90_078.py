N, M = map(int, input().split())

E = [list() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    E[b-1].append(a-1)

ans = 0
for i in range(N):
    if len(E[i]) == 1:
        ans += 1
print(ans)
