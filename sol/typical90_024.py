N, K = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

for a, b in zip(A, B):
    K -= abs(a - b)

if K < 0:
    print("No")
elif K % 2 == 0:
    print("Yes")
else:
    print("No")
