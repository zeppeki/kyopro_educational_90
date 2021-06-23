import itertools

N = int(input())

def check(s):
    cnt = 0
    for c in s:
        if c == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

ans = []
S = itertools.product("()", repeat=N)
for s in S:
    if check(s):
        ans.append("".join(s))
for s in sorted(ans):
    print(s)
