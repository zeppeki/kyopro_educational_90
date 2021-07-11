import math

N = int(input())

cnt = 0
for i in range(2, int(math.sqrt(N)) + 2):
    while N % i == 0:
        N //= i
        cnt += 1
if N > 1:
    cnt += 1

print(math.ceil(math.log2(cnt)))
