N = int(input())
S = input()

k = 0
ans = N * (N-1) // 2
for i in range(N-1):
    if S[i] == S[i+1]:
        k += 1
    else:
        ans -= k * (k+1) // 2
        k = 0

ans -= k * (k+1) // 2
print(ans)
