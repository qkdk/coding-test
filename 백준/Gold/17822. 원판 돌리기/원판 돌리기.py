import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())

matrix = []
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def turnLeft(q: deque, k):
    for _ in range(k):
        q.append(q.popleft())


def turnRight(q: deque, k):
    for _ in range(k):
        q.appendleft(q.pop())


# def dfs(target, y, x, visited):
#     visited[y][x] = True
#     count = 0
#
#     for d in vector:
#         ny = y + d[0]
#         nx = x + d[1]
#
#         if nx == m:
#             nx = 0
#         if nx == -1:
#             nx = m - 1
#         if ny < 0 or ny >= n:
#             continue
#         if matrix[ny][nx] != target:
#             continue
#         if visited[ny][nx] == False:
#             count += 1
#             visited[ny][nx] = True
#             matrix[ny][nx] = 0
#             matrix[y][x] = 0
#             count += dfs(target, ny, nx, visited)
#
#     return count

def checkMatrix():
    global matrix
    count = 0
    cpMatrix = [deque([0] * m) for _ in range(n)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue

            for d in vector:
                ny = i + d[0]
                nx = j + d[1]

                if ny < 0 or ny >= n:
                    continue
                if nx < 0:
                    nx = m - 1
                if nx == m:
                    nx = 0

                if matrix[ny][nx] == matrix[i][j]:
                    count += 1
                    cpMatrix[i][j] = 0
                    break
            else:
                cpMatrix[i][j] = matrix[i][j]
    matrix = cpMatrix
    return count


def re():
    summ = 0
    count = 0

    for row in matrix:
        for v in row:
            if v != 0:
                count += 1
                summ += v
    if count == 0:
        return
    avg = summ / count

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue
            if matrix[i][j] > avg:
                matrix[i][j] -= 1
            elif matrix[i][j] < avg:
                matrix[i][j] += 1


def result():
    result = 0
    for row in matrix:
        result += sum(row)
    return result


for _ in range(n):
    matrix.append(deque(list(map(int, input().strip().split()))))

for _ in range(t):
    x, d, k = map(int, input().split())

    if d == 0:
        for i in range(x - 1, len(matrix), x):
            turnRight(matrix[i], k)
    else:
        for i in range(x - 1, len(matrix), x):
            turnLeft(matrix[i], k)

    count = checkMatrix()

    if count == 0:
        re()
print(result())