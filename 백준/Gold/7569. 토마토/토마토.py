import sys
from collections import deque

input = sys.stdin.readline

vector = ((0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0))

n, m, h = map(int, input().split())


def bfs(matrix, tomato):
    answer = 0
    q = deque(tomato)

    while q:
        cur = q.popleft()
        ch = cur[0]
        cy = cur[1]
        cx = cur[2]
        depth = cur[3]
        answer = max(depth, answer)

        for d in vector:
            nh = ch + d[0]
            ny = cy + d[1]
            nx = cx + d[2]

            if nh < 0 or nh >= len(matrix) or ny < 0 or ny >= len(matrix[0]) or nx < 0 or nx >= len(matrix[0][0]):
                continue

            if matrix[nh][ny][nx] == 1:
                continue

            if matrix[nh][ny][nx] == -1:
                continue

            matrix[nh][ny][nx] = 1
            q.append((nh, ny, nx, depth + 1))

    for s in matrix:
        for row in s:
            for v in row:
                if v == 0:
                    return -1

    return answer


matrix = []
tomato = []

for k in range(h):
    matrix.append([])
    for j in range(m):
        line = list(map(int, input().split()))
        for i, v in enumerate(line):
            if v == 1:
                tomato.append((k, j, i, 0))

        matrix[k].append(line)

print(bfs(matrix, tomato))