# 팀장에서 자식들의 값중 최소 값을 판단해야한다.
# 팀장 자신을 뽑는 경우, 안뽑는 경우 해서 값 저장 dp 에
# 뽑는 경우는 자식들을 안뽑았을 경우 더해야 하는 값들 추가 해줌 , 자기 자신도
# 안뽑는 경우는 자식들중 뽑는경우 + 나머지 안뽑는 경우의 최소값을 넣어준다.
import sys

sys.setrecursionlimit(300001)

def solution(sales, links):
    tree = {}
    for i in range(1, len(sales) + 1):
        tree[i] = []
    
    for u, v in links:
        tree[u].append(v)
    
    dp = [[0, 0] for _ in range(len(sales) + 1)]
    dfs(tree, 1, dp, sales)
    return min(dp[1])

def dfs(tree, start, dp, sales):
    nexts = tree[start]
    
    dp[start][0] = sales[start - 1]
    
    for next in nexts:
        dfs(tree, next, dp, sales)
        
    # 자기를 선택하는 경우
    # 하위 자식들을 선택하지(혹은 선택) 않았을 경우의 값들 더하기
    for next in nexts:
        dp[start][0] += min(dp[next][0], dp[next][1])
        
    # 자기를 선택하지 않았을 경우
    # 자식들중 하나는 선택되어야 함
    # 하나씩 선택해봄
    if nexts:
        minV = float('inf')
        for i in nexts:
            tmp = 0
            for j in nexts:
                if i == j:
                    tmp += dp[i][0]
                else:
                    tmp += min(dp[j][0], dp[j][1])

            minV = min(minV, tmp)
        dp[start][1] = minV
        # print(minV)
        
        