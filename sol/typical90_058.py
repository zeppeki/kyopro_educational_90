N, K = map(int, input().split())

L = [N]
S = set(L)

def f(x):
    y = sum(list(map(int, list(str(x)))))
    z = (x + y) % 100000
    return z

x = N
for i in range(K):
    x = f(x)
    if x in S:
        idx = L.index(x)
        p = len(L) - idx
        q = (K - i - 1) % p
        print(L[idx + q])
        exit(0)
    else:
        L.append(x)
        S.add(x)
print(L[-1])
