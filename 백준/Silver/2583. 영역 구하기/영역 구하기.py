import sys
sys.setrecursionlimit(10000)  # 재귀 한도 증가

input = sys.stdin.readline

m, n, k = map(int, input().strip().split())

matrix = [[0] * n for _ in range(m)]

for i in range(k):
    lx, ly, rx, ry = map(int, input().strip().split())

    ly = m - ly
    ry = m - ry

    for y in range(ry, ly):
        for x in range(lx, rx):
            matrix[y][x] = 1


vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(x, y):
    count = 0

    matrix[y][x] = -1  # 방문한 곳을 표시

    for v in vector:
        nx = x + v[0]
        ny = y + v[1]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or matrix[ny][nx] != 0:
            continue

        count += dfs(nx, ny)

    return count + 1

answer = []
for y in range(m):
    for x in range(n):
        if matrix[y][x] == 0:
            answer.append(dfs(x, y))

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))