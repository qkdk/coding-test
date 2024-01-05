import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

vector = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))


def bfs(visited, sy, sx, dy, dx):
    q = deque()
    q.append((sy, sx, 0))
    visited[sy][sx] = True

    while q:
        cur = q.popleft()
        cy = cur[0]
        cx = cur[1]
        cd = cur[2]

        if cy == dy and cx == dx:
            return cd

        for d in vector:
            ny = cy + d[0]
            nx = cx + d[1]

            if ny < 0 or len(visited) <= ny or nx < 0 or len(visited[0]) <= nx:
                continue
            if visited[ny][nx]:
                continue

            visited[ny][nx] = True
            q.append((ny, nx, cd + 1))


for _ in range(tc):
    l = int(input())
    visited = [[False] * l for _ in range(l)]

    sy, sx = map(int, input().split())
    dy, dx = map(int, input().split())
    print(bfs(visited, sy, sx, dy, dx))