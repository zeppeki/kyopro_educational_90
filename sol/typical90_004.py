H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

X = [0] * H
Y = [0] * W
for i in range(H):
    for j in range(W):
        X[i] += A[i][j]
        Y[j] += A[i][j]

for i in range(H):
    v = []
    for j in range(W):
        v.append(X[i] + Y[j] - A[i][j])
    print(*v, sep=" ")
