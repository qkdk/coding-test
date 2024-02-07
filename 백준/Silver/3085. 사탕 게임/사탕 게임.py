import sys

input = sys.stdin.readline

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input().strip()))


def check(lst):
    tmpCount = 1
    maxCount = 1

    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            tmpCount += 1
            maxCount = max(maxCount, tmpCount)
        else:
            tmpCount = 1

    return maxCount


def solve():
    answer = 0

    for i in range(n):
        for j in range(n - 1):
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            answer = max(answer, check(matrix[i]), check([matrix[x][j] for x in range(n)]),
                         check([matrix[x][j + 1] for x in range(n)]))
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]

    for i in range(n):
        for j in range(n - 1):
            matrix[j][i], matrix[j + 1][i] = matrix[j + 1][i], matrix[j][i]
            answer = max(answer, check(matrix[j]), check(matrix[j + 1]), check([matrix[x][i] for x in range(n)]))
            matrix[j][i], matrix[j + 1][i] = matrix[j + 1][i], matrix[j][i]

    return answer


print(solve())