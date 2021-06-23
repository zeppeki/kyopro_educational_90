N = int(input())

A = [0] * N
B = [0] * N
X = [A, B]

for i in range(N):
    c, p = map(int, input().split())
    X[c-1][i] = p

C = [0] * (N+1)
D = [0] * (N+1)
for i in range(1, N+1):
    C[i] = C[i-1] + A[i-1]
    D[i] = D[i-1] + B[i-1]

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    print(C[R] - C[L-1], D[R] - D[L-1])
