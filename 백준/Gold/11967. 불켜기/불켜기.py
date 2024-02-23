import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())

dic = {}
matrix = [[False] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for _ in range(m):
    x, y, a, b = map(int, input().strip().split())
    if (y - 1, x - 1) in dic:
        dic[(y - 1, x - 1)].append((b - 1, a - 1))
    else:
        dic[(y - 1, x - 1)] = [(b - 1, a - 1)]


def bfs(y, x):
    q = deque()
    visited[y][x] = True
    matrix[y][x] = True
    q.append((y, x))

    while q:
        cur = q.popleft()

        if cur in dic:
            for ny, nx in dic[cur]:
                if visited[ny][nx] == True:
                    continue
                matrix[ny][nx] = True
                for d in vector:
                    nny = ny + d[0]
                    nnx = nx + d[1]

                    if nny < 0 or nnx < 0 or nny >= n or nnx >= n:
                        continue

                    if matrix[nny][nnx] == True and visited[nny][nnx] == True:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        break

        for d in vector:
            ny = cur[0] + d[0]
            nx = cur[1] + d[1]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            if matrix[ny][nx] == True and visited[ny][nx] == False:
                q.append((ny, nx))
                visited[ny][nx] = True


def solve():
    bfs(0, 0)

    result = 0
    for row in matrix:
        for v in row:
            if v == True:
                result += 1
    return result

print(solve())