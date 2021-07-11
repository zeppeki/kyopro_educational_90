import math

K = int(input())

N = int(math.sqrt(K)) + 1
ans = 0
for a in range(1, N):
    if K % a != 0:
        continue
    M = int(math.sqrt(K // a)) + 1
    for b in range(a, M + 1):
        if K % b != 0:
            continue
        c = K // a // b
        if c >= b and a * b * c == K:
            ans += 1
print(ans)
