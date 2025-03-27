import sys

sys.setrecursionlimit(100000)  # 재귀 한도 증가
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
matrix = [[0] * n for _ in range(n)]

for _ in range(k):
    y, x = map(int, input().strip().split())
    y, x = y - 1, x - 1
    matrix[y][x] = 1

l = int(input())
actions = deque()
for _ in range(l):
    t, c = input().strip().split()
    c = 1 if c == 'D' else -1  # D면 1, L이면 -1
    actions.append((int(t), c))

vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]
snake = deque()
snake.append((0, 0))

cur_dir = 1
for cur_time in range(1, 10001):
    head = snake[0]

    dy, dx = vector[cur_dir]
    ny, nx = head[0] + dy, head[1] + dx
    if ny < 0 or ny >= n or nx < 0 or nx >= n or (ny, nx) in snake:
        print(cur_time)
        break

    snake.appendleft((ny, nx))

    if matrix[ny][nx] == 1:
        matrix[ny][nx] = 0
    else:
        snake.pop()

    # 방향 전환
    if actions and int(actions[0][0]) == cur_time:
        cur_dir = (cur_dir + actions[0][1]) % 4
        actions.popleft()
