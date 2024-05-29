# 라벨링 하고 진행
from collections import deque

vector = [[-1,0],[0,1],[1,0],[0,-1]]
def solution(land):
    # visited = [[False] * len(land[0]) for _ in range(len(land))]
    # 라벨링 작업
    dic = {}
    label = 2
    for y in range(len(land)):
        for x in range(len(land[0])):            
            if land[y][x] == 1:
                bfs(y,x, land, label, dic)
                label += 1
    
    # print(dic)
    # printMatrix(land)
    
    # 탐색
    answer = 0
    for x in range(len(land[0])):
        tmp = 0
        visited = [False] * (len(dic) + 2)
        
        for y in range(len(land)):
            if land[y][x] >= 2:
                label = land[y][x]
                if visited[label]:
                    continue
                visited[label] = True
                tmp += dic[label]
        answer = max(answer, tmp)
        
    # answer = 0
    return answer

def bfs(y, x, land, label, dic):
    land[y][x] = label
    count = 0
    q = deque()
    q.append((y,x))

    while q:
        y, x = q.popleft()
        count += 1

        for d in vector:
            ny = y + d[0]
            nx = x + d[1]

            if ny < 0 or nx < 0 or ny >= len(land) or nx >= len(land[0]):
                continue
            if land[ny][nx] != 1:
                continue

            land[ny][nx] = label
            q.append((ny,nx))
            
    dic[label] = count

def printMatrix(matrix):
    for row in matrix:
        print(row)