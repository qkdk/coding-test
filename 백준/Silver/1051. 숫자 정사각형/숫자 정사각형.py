import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().strip())))

length = min(n, m)

for l in range(length - 1, -1, -1):
    for y in range(0, n - l):
        for x in range(0, m - l):
            if matrix[y][x] == matrix[y + l][x] == matrix[y][x + l] == matrix[y + l][x + l]:
                print((l + 1) ** 2)
                exit(0)