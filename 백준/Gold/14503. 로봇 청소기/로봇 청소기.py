import sys
sys.setrecursionlimit(100000)  # 재귀 한도 증가
input = sys.stdin.readline

n,m = map(int,input().strip().split())
r, c, d = map(int,input().strip().split())
matrix = [list(map(int,input().strip().split())) for _ in range(n)]
vector = [[-1,0],[0,1],[1,0],[0,-1]]

count = 0
def dfs(y, x, d):
    # 현재칸 청소
    global count, matrix

    if matrix[y][x] == 0:
        matrix[y][x] = 2
        count += 1

    # 4방향 체크
    need_clean = False
    for dir in vector:
        ny = y + dir[0]
        nx = x + dir[1]

        if matrix[ny][nx] == 0:
            need_clean = True

    # 4방향 모두 청소가 안되어 있는 경우
    if need_clean:
        # 현재 방향 기준 왼쪽 방향
        d = (d - 1) % 4
        dy, dx = vector[d]
        ny = y + dy
        nx = x + dx
        if matrix[ny][nx] == 0:
            dfs(ny, nx, d)
        else:
            dfs(y, x, d)

    # 4방향 모두 청소가 되어 있는 경우
    else:
        nd = (d + 2) % 4
        dy, dx = vector[nd]
        ny = y + dy
        nx = x + dx
        if matrix[ny][nx] != 1:
            dfs(ny, nx, d)
        else:
            return

dfs(r,c,d)
print(count)

