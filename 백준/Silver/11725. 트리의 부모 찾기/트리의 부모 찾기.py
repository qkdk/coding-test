import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = {i: [] for i in range(1, n + 1)}
visited = [False] * (n + 1)
visited[1] = True

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0 for _ in range(n + 1)]


def bfs():
    q = deque()
    q.append((1, 0))

    while q:
        cur = q.popleft()

        parents[cur[0]] = cur[1]
        for v in graph[cur[0]]:
            if not visited[v]:
                visited[v] = True
                q.append((v, cur[0]))


bfs()

answer = '\n'.join(map(str, parents[2:]))
print(answer)