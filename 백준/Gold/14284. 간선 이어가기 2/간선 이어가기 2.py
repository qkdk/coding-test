import sys
import heapq

INF = float('inf')
input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i + 1: [] for i in range(n)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

s, e = map(int, input().split())
# dijk

dist = [INF] * (n + 1)
dist[s] = 0
q = []
heapq.heappush(q, (0, s))

while q:
    cost, cur = heapq.heappop(q)

    for nCost, nIdx in graph[cur]:
        if dist[nIdx] > nCost + cost:
            dist[nIdx] = nCost + cost
            heapq.heappush(q, (dist[nIdx], nIdx))

print(dist[e])