import heapq
def dijkstra(K):
    q = []
    heapq.heappush(q, (0, K))
    D[K] = 0

    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:
           continue
        for i in adjM[now]:
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


V, E = map(int, input().split())
K = int(input())
INF = 200000
adjM = [[]*(V+1) for _ in range(V+1)]
D = [INF]*(V+1)
for _ in range(E):
    a, b, c = map(int, input().split())
    adjM[a].append((b, c))

dijkstra(K)
for i in range(1, V+1):
    if D[i] == INF:
        print("INF")
    else:
        print(D[i])