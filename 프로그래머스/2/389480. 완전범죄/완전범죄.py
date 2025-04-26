'''
1. 완전 탐색을 하는 방법 2 **40 -> 불가능
2. 그리디 -> A, B 조건 두개 불가능
3. DP -> 냅색문제

플이
dp = [i][j]
i 는 아이템, j는 B의 흔적
A를 선택한 경우 dp[i][j] = dp[i -1][j] + A의 흔적
B를 선택한 경우 dp[i][j + B의 흔적] = dp[i- 1][j]

어려운점
A 와 B를 선택하는 경우 두개로 나누어서
B를 선택하는경우 dp[i][j]가 아닌 dp[i][j + b]를 업데이트 해줘야함
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
