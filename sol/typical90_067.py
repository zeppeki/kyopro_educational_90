N, K = map(int, input().split())

def octto9th(x):
    if x == "0":
        return x
    x = int(x, base=8)
    ans = []
    while x > 0:
        x, q = divmod(x, 9)
        ans.append(str(q))
    return("".join(ans[::-1]))

N = str(N)
for k in range(K):
    y = octto9th(N)
    N = y.replace("8", "5")
print(N)
