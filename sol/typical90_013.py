import heapq

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A-1].append((C, B-1))
    G[B-1].append((C, A-1))

def dijkstra(G, s):
    dist = [-1 for _ in range(N)]
    done = [False for _ in range(N)]
    Q = []

    heapq.heappush(Q, (0, s))
    dist[s] = 0

    while len(Q) > 0:
        (d, i) = heapq.heappop(Q)
        if done[i]:
            continue
        done[i] = True
        for c, j in G[i]:
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(Q, (dist[j], j))
    return dist

d1 = dijkstra(G, 0)
d2 = dijkstra(G, N-1)

for i in range(N):
    print(d1[i] + d2[i])
