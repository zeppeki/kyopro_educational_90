N = int(input())
A, B, C = map(int, input().split())

ans = 10000
for a in range(min(N // A + 2, 10000)):
    u = N - a * A
    for b in range(min(u // B + 2, 10000-a)):
        if a + b > ans:
            continue
        v = u - b * B
        if v < 0 or v % C != 0:
            continue
        c = v // C
        ans = min(ans, a+b+c)
print(ans)
