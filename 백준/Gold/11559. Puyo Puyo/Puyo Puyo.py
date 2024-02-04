import sys
from collections import deque

input = sys.stdin.readline

matrix = []
for _ in range(12):
    matrix.append(list(input().strip()))

vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(visited, y, x):
    q = deque()
    q.append((y, x))

    value = matrix[y][x]
    result = []
    visited[y][x] = True

    while q:
        cy, cx = q.popleft()
        result.append((cy, cx))

        for dy, dx in vector:
            ny = cy + dy
            nx = cx + dx

            if ny < 0 or ny >= 12 or nx < 0 or nx >= 6:
                continue

            if visited[ny][nx]:
                continue

            if matrix[ny][nx] == value:
                q.append((ny, nx))
                visited[ny][nx] = True

    return result


def puyo():
    visited = [[False] * 6 for _ in range(12)]
    endFlag = True
    for y in range(12):
        for x in range(6):
            if matrix[y][x] != '.' and visited[y][x] == False:
                result = bfs(visited, y, x)
                if len(result) >= 4:
                    endFlag = False
                    for ty, tx in result:
                        matrix[ty][tx] = '.'

    return endFlag


def swap(y1, y2, x):
    temp = matrix[y1][x]
    matrix[y1][x] = matrix[y2][x]
    matrix[y2][x] = temp



def fall():
    for x in range(0, 6):
        spaceIdx = -1
        for y in range(11, -1, -1):
            if matrix[y][x] == '.' and spaceIdx == -1:
                spaceIdx = y
            if matrix[y][x] != '.' and spaceIdx != -1:
                swap(spaceIdx, y, x)
                spaceIdx -= 1


def solve():
    answer = 0
    endFlag = False

    while True:
        endFlag = puyo()
        if endFlag == True:
            break
        fall()
        answer += 1

    print(answer)


solve()