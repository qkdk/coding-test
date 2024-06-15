import sys

input = sys.stdin.readline

n, m, k = map(int, input().strip().split())
matrix = [[[] for _ in range(n)] for _ in range(n)]

vector = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(m):
    r, c, m, s, d = map(int, input().strip().split())
    r -= 1
    c -= 1

    matrix[r][c].append([m, s, d])


def move():
    global matrix

    cpMatrix = [[[] for _ in range(n)] for _ in range(n)]

    for y, row in enumerate(matrix):
        for x, vs in enumerate(row):
            for v in vs:
                m, s, d = v
                ny = (y + s * vector[d][0]) % n
                nx = (x + s * vector[d][1]) % n

                cpMatrix[ny][nx].append(v)

    matrix = cpMatrix


def dist():
    for row in matrix:
        for vs in row:
            if len(vs) >= 2:
                nm = 0
                ns = 0
                nd = 0

                for v in vs:
                    nm += v[0]
                nm //= 5

                if nm == 0:
                    vs.clear()
                    continue

                for v in vs:
                    ns += v[1]
                ns //= len(vs)

                std = vs[0][2] % 2
                for i in range(1, len(vs)):
                    if vs[i][2] % 2 != std:
                        nd = 1
                        break

                vs.clear()
                for _ in range(4):
                    vs.append([nm, ns, nd])
                    nd += 2


def solve():
    for _ in range(k):
        move()
        dist()

    answer = 0
    for row in matrix:
        for vs in row:
            for v in vs:
                answer += v[0]

    return answer


print(solve())