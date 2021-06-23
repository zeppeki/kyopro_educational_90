import statistics

N = int(input())

X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

xm = statistics.median(X)
ym = statistics.median(Y)
ans = 0
for x in X:
    ans += abs(x - xm)
for y in Y:
    ans += abs(y - ym)
print(int(ans))
