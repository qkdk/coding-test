import sys
import heapq

INF = float('inf')
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = {i + 1: [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))

dist = [INF] * (n + 1)

q = []
dist[x] = 0

heapq.heappush(q, (0, x))

while q:
    cost, cur = heapq.heappop(q)

    for nCost, nIdx in graph[cur]:
        if dist[nIdx] > nCost + cost:
            dist[nIdx] = nCost + cost
            heapq.heappush(q, (dist[nIdx], nIdx))

flag = False
for i, v in enumerate(dist):
    if v == k:
        print(i)
        flag = True
if not flag:
    print(-1)