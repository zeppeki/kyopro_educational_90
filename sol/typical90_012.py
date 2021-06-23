H, W = map(int, input().split())
Q = int(input())

class dsu:
    def __init__(self, N):
        self.root = [-1 for _ in range(N)]
        self.size = [1 for _ in range(N)]

    def merge(self, x, y):
        x = self.leader(x)
        y = self.leader(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.root[x] = y
            self.size[y] += self.size[x]
        else:
            self.root[y] = x
            self.size[x] += self.size[y]
    
    def leader(self, x):
        while self.root[x] >= 0:
            x = self.root[x]
        return x

    def same(self, x, y):
        return self.leader(x) == self.leader(y)

uf = dsu(H * W)
red = [False for _ in range(H * W)]

for _ in range(Q):
    q, *val = list(map(int, input().split()))
    if q == 1:
        r, c = [v - 1 for v in val]
        x = r * W + c
        red[x] = True
        if r > 0 and red[x-W]:
            uf.merge(x, x - W)
        if r < H-1 and red[x+W]:
            uf.merge(x, x + W)
        if c > 0 and red[x-1]:
            uf.merge(x, x - 1)
        if c < W-1 and red[x+1]:
            uf.merge(x, x + 1)
    else:
        ra, ca, rb, cb = [v - 1 for v in val]
        x = ra * W + ca
        y = rb * W + cb
        if not red[x]:
            print("No")
        elif uf.same(x, y):
            print("Yes")
        else:
            print("No")
