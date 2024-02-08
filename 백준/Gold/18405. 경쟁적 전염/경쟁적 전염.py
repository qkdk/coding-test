import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

s, y, x = map(int, input().split())
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

q = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            # 종류, y, x 순으로 입력
            heapq.heappush(q, (0, matrix[i][j], i, j))

while q:
    l, cv, cy, cx = heapq.heappop(q)
    if l == s:
        break

    for dy, dx in vector:
        ny = cy + dy
        nx = cx + dx
        if ny < 0 or nx < 0 or ny >= len(matrix) or nx >= len(matrix[0]):
            continue
        if matrix[ny][nx] != 0:
            continue
        matrix[ny][nx] = cv
        heapq.heappush(q, (l + 1, matrix[ny][nx], ny, nx))

print(matrix[y - 1][x - 1])