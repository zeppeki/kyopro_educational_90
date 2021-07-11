import collections

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())

S = [input() for _ in range(H)]

INF = 10 ** 10
dp = [[[INF] * W for _ in range(H)] for _ in range(4)]
q = collections.deque()

rs -= 1
cs -= 1
rt -= 1
ct -= 1

for d in range(4):
    dp[d][rs][cs] = 0
    q.append((d, rs, cs))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while len(q) > 0:
    d, r, c = q.popleft()
    v = dp[d][r][c]  
    for k in range(4):
        if dp[k][r][c] > v + 1:
            dp[k][r][c] = v + 1
            q.append((k, r, c))

    rd, cd = move[d]
    rx, cx = r + rd, c + cd
    if rx < 0 or rx >= H or cx < 0 or cx >= W or S[rx][cx] == "#": continue
    if dp[d][rx][cx] > v:
        dp[d][rx][cx] = v
        q.appendleft((d, rx, cx))

ans = INF
for d in range(4):
    ans = min(ans, dp[d][rt][ct])
print(ans)
