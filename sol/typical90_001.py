N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(x):
    k = 0
    v = 0
    for a in A:
        if a - v >= x:
            k += 1
            v = a
    if L - v < x:
        k -= 1
    return k >= K

ok = 0
ng = L
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
