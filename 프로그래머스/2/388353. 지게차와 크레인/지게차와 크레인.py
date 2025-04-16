import copy

vector = [[-1, 0],[0,1],[1,0],[0,-1]]

def solution(storage, requests):
    matrix = []
    for row in storage:
        matrix.append(list(row))
    
    for request in requests:
        if len(request) == 1:
            matrix = boundary_check(request, matrix)
        else:
            remove_all(request[0], matrix)
    
        # print_matrix(matrix)
    answer = sum_matrix(matrix)
    return answer

def print_matrix(matrix):
    for row in matrix:
        print(row)

def sum_matrix(matrix):
    count = 0
    for row in matrix:
        for v in row:
            if v != 0:
                count += 1
    return count
        

def remove_all(target, matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == target:
                matrix[y][x] = 0

def boundary_check(target, matrix):
    cp_matrix = copy.deepcopy(matrix)
    
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == target:
                visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
                visited[y][x] = True
                
                result = dfs(y, x, matrix, visited)
                if result:
                    cp_matrix[y][x] = 0

                        
    return cp_matrix

def dfs(y, x, matrix, visited):
    result = False
    
    for d in vector:
        dy = d[0]
        dx = d[1]
        
        ny = y + dy
        nx = x + dx
        
        if ny < 0 or nx < 0 or ny >= len(matrix) or nx >= len(matrix[0]):
            return True
        
        if visited[ny][nx]:
            continue
        
        if matrix[ny][nx] == 0:
            visited[ny][nx] = True
            result = result or dfs(ny, nx, matrix, visited)
    
    return result