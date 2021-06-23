N, K = map(int, input().split())

X = []
for _ in range(N):
    A, B = map(int, input().split())
    X.append(B)
    X.append(A-B)
X.sort()
print(sum(X[-K:]))
