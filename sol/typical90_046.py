N = int(input())
A = map(int, input().split())
B = map(int, input().split())
C = map(int, input().split())

X = [0 for _ in range(46)]
Y = [0 for _ in range(46)]
Z = [0 for _ in range(46)]

for a in A:
    X[a % 46] += 1
for b in B:
    Y[b % 46] += 1
for c in C:
    Z[c % 46] += 1

ans = 0
for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a + b + c) % 46 == 0:
                ans += X[a] * Y[b] * Z[c]
print(ans) 

