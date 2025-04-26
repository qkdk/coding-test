'''
1. 완전 탐색을 하는 방법 2 **40 -> 불가능
2. 그리디 -> A, B 조건 두개 불가능
3. DP -> 
'''

def solution(info, n, m):
    
    dp = [[99999] * m for _ in range(len(info) + 1)]
    dp[0][0] = 0
    
    for i in range(1, len(info) + 1):
        a, b = info[i - 1]
        
        for j in range(0, m):
            dp[i][j] = min(dp[i -1][j] + a, dp[i][j])
            
            if j + b < m:
                dp[i][j + b] = min(dp[i -1][j], dp[i][j + b])
    
    answer = 0
    # print_matrix(dp)
    
    r = min(dp[-1])
    if r < n:
        answer = r
    else :
        answer = -1
    return answer

def print_matrix(matrix):
    for row in matrix:
        print(row)
