import sys

input = sys.stdin.readline

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input().strip()))


def check():
    maxCount = 0

    for i in range(n):
        tmpCount = 1
        for j in range(1, n):
            if matrix[i][j] == matrix[i][j - 1]:
                tmpCount += 1
            else:
                maxCount = max(maxCount, tmpCount)
                tmpCount = 1
        maxCount = max(maxCount, tmpCount)

    for i in range(n):
        tmpCount = 1
        for j in range(1, n):
            if matrix[j][i] == matrix[j - 1][i]:
                tmpCount += 1
            else:
                maxCount = max(maxCount, tmpCount)
                tmpCount = 1
        maxCount = max(maxCount, tmpCount)

    return maxCount


def solve():
    answer = check()

    for i in range(n):
        for j in range(n - 1):
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            answer = max(answer, check())
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]

    for i in range(n):
        for j in range(n - 1):
            matrix[j][i], matrix[j + 1][i] = matrix[j + 1][i], matrix[j][i]
            answer = max(answer, check())
            matrix[j][i], matrix[j + 1][i] = matrix[j + 1][i], matrix[j][i]

    return answer


print(solve())