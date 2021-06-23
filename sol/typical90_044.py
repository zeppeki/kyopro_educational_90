N, Q = map(int, input().split())
A = list(map(int, input().split()))

s = 0
for _ in range(Q):
    T, x, y = map(int, input().split())
    u = (x-1+s) % N
    v = (y-1+s) % N
    if T == 1:
        A[u], A[v] = A[v], A[u]
    elif T == 2:
        s -= 1
    else:
        print(A[u])
