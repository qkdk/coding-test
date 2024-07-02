import sys

input = sys.stdin.readline

matrix = []
for _ in range(5):
    lst = list(map(int, input().strip().split()))
    matrix.append(lst)

vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

st = set()


def dfs(y, x, depth, cur):
    if depth == 5:
        st.add(cur)
        return

    for d in vector:
        ny = y + d[0]
        nx = x + d[1]

        if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
            continue

        dfs(ny, nx, depth + 1, cur * 10 + matrix[ny][nx])


for y in range(5):
    for x in range(5):
        dfs(y, x, 0, matrix[y][x])

print(len(st))