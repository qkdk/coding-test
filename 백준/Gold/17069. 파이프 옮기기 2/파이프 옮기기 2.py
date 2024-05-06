import sys

input = sys.stdin.readline


def print_matrix(matrix):
    for r in matrix:
        for row in r:
            print(row)
        print()


n = int(input())

vector = [[1, 0], [0, 1], [1, 1]]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

matrix = []
for _ in range(n):
    line = list(map(int, input().strip().split()))
    matrix.append(line)


# 0 가로 1 세로 2 대각선

def cross(y, x):
    for d in vector:
        ny = y + d[0]
        nx = x + d[1]
        if not (ny < 0 or nx < 0 or ny >= n or nx >= n):
            if matrix[ny][nx] == 1:
                return False
    return True


for y in range(n):
    for x in range(1, n):
        ny = y
        nx = x + 1
        if not (ny < 0 or nx < 0 or ny >= n or nx >= n):
            if matrix[ny][nx] != 1:
                dp[0][y][x + 1] += dp[0][y][x]

        if cross(y, x):
            nx = x + 1
            ny = y + 1
            if not (ny < 0 or nx < 0 or ny >= n or nx >= n):
                dp[2][y + 1][x + 1] += dp[0][y][x]

        ny = y + 1
        nx = x
        if not (ny < 0 or nx < 0 or ny >= n or nx >= n):
            if matrix[ny][nx] != 1:
                dp[1][y + 1][x] += dp[1][y][x]

        if cross(y, x):
            ny = y + 1
            nx = x + 1
            if not (ny < 0 or nx < 0 or ny >= n or nx >= n):
                dp[2][y + 1][x + 1] += dp[1][y][x]

        ny = y
        nx = x + 1
        if not (ny < 0 or nx < 0 or ny >= n or nx >= n):
            if matrix[ny][nx] != 1:
                dp[0][y][x + 1] += dp[2][y][x]
        ny = y + 1
        nx = x
        if not (ny < 0 or nx < 0 or ny >= n or nx >= n):
            if matrix[ny][nx] != 1:
                dp[1][y + 1][x] += dp[2][y][x]

        if cross(y, x):
            ny = y + 1
            nx = x + 1
            if not (ny < 0 or nx < 0 or ny >= n or nx >= n):
                dp[2][y + 1][x + 1] += dp[2][y][x]

print(dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1])