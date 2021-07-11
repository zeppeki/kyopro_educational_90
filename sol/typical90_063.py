from collections import Counter

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for x in range(1<<H):
    cnt = Counter()
    for j in range(W):
        v = None
        k = 0
        for i in range(H):
            if (x>>i) & 1:
                k += 1
                if v is None:
                    v = P[i][j]
                elif v != P[i][j]:
                    v = -1
        if v is not None and v > 0:
            cnt[v] += k
    if len(cnt) > 0:
        a = cnt.most_common()[0][1]
        ans = max(ans, a)
print(ans)
