# 우선 사각형을 matrix에 다 그린다. 빈칸을 채워서 1로
# 모든 좌표를 사방탐색 진행해서 새로운 matrix를 그려야한다.
# 1이 채워져있는곳에서 주변 모두 1이 있다면 안쪽 -> 옮기기 X
# 아니라면 옮기기
# 이후 시작점에서 팔방탐색 진행
# 상하좌우로 이동한 경우 1, 대각선으로 이동한 경우 2 -> 가로 세로 이동 벡터의 절대값을 이용
from collections import deque

matrix_size = 102
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    matrix = [[0] * matrix_size for _ in range(matrix_size)]
    
    for coord in rectangle:
        sx, sy, ex, ey = coord
        for y in range(sy * 2, ey * 2 + 1, 1):
            for x in range(sx * 2, ex * 2 + 1, 1):
                matrix[y][x] = 1
                
    # print_matrix(matrix)
        
    vector_4 = [[-1,0],[0,1],[1,0],[0,-1]]
    vector_8 = [[-1,0],[0,1],[1,0],[0,-1],[-1,1],[1,1],[1,-1],[-1,-1]]
    n_matrix = [[0] * matrix_size for _ in range(matrix_size)]
    for y in range(matrix_size):
        for x in range(matrix_size):
            if matrix[y][x] == 1:
                flag = False
                for dy, dx in vector_8:
                    ny = y + dy
                    nx = x + dx
                    
                    if ny < 0 or nx < 0 or ny >= matrix_size or nx >= matrix_size:
                        continue
                    if matrix[ny][nx] == 0:
                        flag = True
                
                if flag:
                    n_matrix[y][x] = 1
    
    # print_matrix(n_matrix)
    # n_matrix[itemY][itemX] = 2
    # bfs
    q = deque()
    visited = [[False] * matrix_size for _ in range(matrix_size)]
    visited[characterY * 2][characterX * 2] = True
    q.append((characterY * 2, characterX * 2, 0))
    
    while q:
        y, x, count = q.popleft()
        
        if y == itemY * 2 and x == itemX * 2:
            
            return count // 2
        
        for dy, dx in vector_4:
            ny, nx = y + dy, x + dx
            
            if ny < 0 or nx < 0 or ny >= matrix_size or nx >= matrix_size:
                continue
            
            if visited[ny][nx]:
                continue
            
            if n_matrix[ny][nx] == 1:
                q.append((ny, nx, count + abs(dy) + abs(dx)))
                visited[ny][nx] = True
            
    answer = 0
    return answer

def print_matrix(matrix):
    for row in matrix:
        print(row)