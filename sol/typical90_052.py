N = int(input())
A = [map(int, input().split()) for _ in range(N)]

ans = 1
for a in A:
    ans *= sum(a)
    ans %= 10 ** 9 + 7
print(ans)
