from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = {}
visited = [False] * (n + 1)


class Pair:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth

    def __str__(self):
        return f"Value: {self.value}, Depth: {self.depth}"

    def __repr__(self):
        return f"Pair(Value: {self.value}, Depth: {self.depth})"


def bfs(start, target):
    q = deque([Pair(start, 0)])
    while q:
        cur = q.popleft()
        if cur.value == target:
            return cur.depth

        visited[cur.value] = True
        for next in graph[cur.value]:
            if visited[next]:
                continue
            q.append(Pair(next, cur.depth + 1))

    return -1


for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = bfs(a, b)
print(answer)