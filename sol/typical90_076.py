N = int(input())
A = list(map(int, input().split()))

p, r = divmod(sum(A), 10)
if r != 0:
    print("No")
    exit(0)
    
X = A + A
j = 0
v = 0
for i in range(2 * N):
    while v < p and j < 2 * N:
        v += X[j]
        j += 1
    if v == p:
        print("Yes")
        exit(0)
    v -= X[i]
print("No")
