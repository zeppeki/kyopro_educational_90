H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for i in range(H-1):
    for j in range(W-1):
        v = B[i][j] - A[i][j]
        for di, dj in [(0,1), (1,0), (1,1)]:
            A[i+di][j+dj] += v
        ans += abs(v)

for i in range(H):
    if B[i][-1] - A[i][-1] != 0:
        print("No")
        exit(0)
for j in range(W):
    if B[-1][j] - A[-1][j] != 0:
        print("No")
        exit(0)
print("Yes")
print(ans)
