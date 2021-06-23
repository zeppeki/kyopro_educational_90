import math

T = int(input())
L, X, Y = map(int, input().split())

Q = int(input())
E = [int(input()) for _ in range(Q)]

for e in E:
    rad = e / T * 2 * math.pi - 1/2 * math.pi
    z = L / 2 * math.sin(rad) + L / 2
    y = L / 2 * math.cos(rad) * -1
    if z == 0:
        ans = 0
    else:
        d = math.sqrt(X**2 + (Y-y)**2)
        ans = math.atan2(z, d) * 180 / math.pi   
    print(ans)
    