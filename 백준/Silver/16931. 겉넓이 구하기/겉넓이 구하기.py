import sys

input = sys.stdin.readline

# 위 아래 2개는 무조건 포함

n, m = map(int, input().strip().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))

# 격자 범위를 벗어나면 갯수만큼 +
# 격자 범위를 벗어나지 않으면, 현재 - 비교 + , 최소 0

vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

answer = 0
for y in range(n):
    for x in range(m):
        # 사방탐색 시작
        for d in vector:
            ny = y + d[0]
            nx = x + d[1]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                answer += matrix[y][x]
            else:
                answer += max(0, matrix[y][x] - matrix[ny][nx])
        answer += 2

print(answer)