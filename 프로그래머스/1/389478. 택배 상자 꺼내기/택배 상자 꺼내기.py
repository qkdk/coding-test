# 그래프를 그린다 없는곳은  -1
# 숫자를 찾는다
# 위에있는거를 없엔다 - x, y 구하고 위로 y

def solution(n, w, num):
    matrix = [[-1] * w for _ in range(n // w + 1)]
    
    y, x = n//w, 0
    dx = +1
    
    for i in range(1, n + 1):
        matrix[y][x] = i
        
        x += dx
        if x == w or x == -1:
            dx = -dx
            x += dx
            y -= 1
    
    # print_matrix(matrix)
    ty, tx = 0,0
    for y in range(len(matrix) -1, -1, -1):
        for x in range(len(matrix[0])):
            if matrix[y][x] == num:
                ty, tx = y, x
    
    # print(ty,tx)
    answer = 0
    
    for y in range(ty, -1, -1):
        if matrix[y][tx] != -1:
            answer += 1
    
    print(answer)
    return answer

def print_matrix(matrix):
    for row in matrix:
        print(row)