N = int(input())
E = [map(int, input().split()) for _ in range(N-1)]

def search(start):
    INF = 1000000
    dist = [INF for _ in range(N)]
    dist[start] = 0
    queue = [start]
    while queue:
        p = queue.pop()
        for t in graph[p]:
            if dist[t] == INF:
                dist[t] = dist[p] + 1
                queue.append(t)
    return(dist)

def maxidx(dist):
    idx = -1
    md = -1
    for i, d in enumerate(dist):
        if md < d:
            idx = i
            md = d
    return(idx)

graph = [[] for _ in range(N)]
for u, v in E:
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

dist = search(0)
idx = maxidx(dist)
dist2 = search(idx)

print(max(dist2) + 1)
