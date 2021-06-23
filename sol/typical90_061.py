Q = int(input())

L = list()
cnt = 0
R = list()

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        L.append(x)
        cnt += 1
    elif t == 2:
        R.append(x)
    else:
        if cnt >= x:
            print(L[-x])
        else:
            print(R[x - cnt - 1])
