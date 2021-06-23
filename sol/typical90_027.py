N = int(input())

U = set()
for i in range(N):
    S = input()
    if S not in U:
        print(i+1)
        U.add(S)
