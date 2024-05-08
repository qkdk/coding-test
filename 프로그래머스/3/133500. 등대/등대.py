import sys

sys.setrecursionlimit(100001)

def solution(n, lighthouse):
    tree = {}
    
    for i in range(1, n + 1):
        tree[i] = []
        
    for u, v in lighthouse:
        tree[u].append(v)
        tree[v].append(u)
        
    visited = [False] * (n + 1)
    visited[1] = True
    dp = [[0] * (n + 1) for _ in range(2)]
    
    dfs(1, visited, dp, tree)
    
    return min(dp[0][1], dp[1][1])

def dfs(start, visited, dp, tree):
    nexts = tree[start]
    
    dp[0][start] = 1
    for next in nexts:
        if visited[next]:
            continue
        visited[next] = True
        
        dfs(next, visited, dp, tree)

        dp[0][start] += min(dp[0][next], dp[1][next])
        dp[1][start] += dp[0][next]
