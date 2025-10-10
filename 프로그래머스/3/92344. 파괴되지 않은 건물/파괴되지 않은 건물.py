# board에 계산을 누적합으로 해결
# 모든 0,0 ~ y,x 까지의 계산 값을 y, x에 저장
# 영향을 안받는 부분ㅇ에는 값의 - 한값을 저장
# 영향을 안받는 부분은 (y1 - 1, x2) , (y2, x1 - 1)

def solution(board, skill):
    answer = 0
    
    cal_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for s_type, y1, x1, y2, x2, degree in skill:
        if s_type == 1:
            degree *= -1
            
        cal_board[y1][x1] += degree
        cal_board[y2 + 1][x2 + 1] += degree
        cal_board[y2 + 1][x1] -= degree
        cal_board[y1][x2 + 1] -= degree
    
    for y in range(len(cal_board)):
        for x in range(len(cal_board[0]) - 1):
            cal_board[y][x + 1] += cal_board[y][x]
            
    for x in range(len(cal_board[0])):
        for y in range(len(cal_board) - 1):
            cal_board[y + 1][x] += cal_board[y][x]
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] += cal_board[y][x]
    
    for row in board:
        for v in row:
            if v > 0 :
                answer += 1
    return answer

        
def print_mat(mat):
    for row in mat:
        print(row)