N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for a, b in zip(sorted(A), sorted(B)):
    ans += abs(a - b)

print(ans)
