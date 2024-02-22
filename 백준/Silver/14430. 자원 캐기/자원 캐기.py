import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))

vector = [[-1, 0], [0, -1]]


def solve():
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):

            maxValue = 0
            for d in vector:
                ny = i + d[0]
                nx = j + d[1]

                if ny < 0 or nx < 0:
                    continue
                maxValue = max(maxValue, dp[ny][nx])
            dp[i][j] = maxValue + matrix[i][j]

    return dp[n - 1][m - 1]


print(solve())