from math import gcd

A, B, C = map(int, input().split())
v = gcd(gcd(A, B), C)

ans = 0
for x in [A, B, C]:
    ans += x // v - 1
print(ans)
