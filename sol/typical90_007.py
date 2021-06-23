N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.append(-(10 ** 10))
A.append(10 ** 10)

A.sort()
Bs = sorted(B)

i = 0
d = dict()
for b in Bs:
    while A[i] < b:
        i += 1
    d[b] = min(b - A[i-1], A[i] - b)

for b in B:
    print(d[b])
