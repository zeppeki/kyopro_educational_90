import math

A, B = map(int, input().split())

v = A * B // math.gcd(A, B)
if v > 10 ** 18:
    print("Large")
else:
    print(v)
