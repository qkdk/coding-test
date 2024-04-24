answer = 1

def solution(info, edges):
    global answer
    
    visited = [False] * len(info)
    visited[0] = True
    
    dfs(info, edges, visited, 1, 0)
    return answer

def dfs(info, edges, visited, sheep, wolf):
    global answer
    
    if sheep == wolf:
        return
    
    answer = max(sheep, answer)
    
    for v in edges:
        if visited[v[0]] == True and visited[v[1]] == False:
            visited[v[1]] = True
            if info[v[1]] == 0:
                dfs(info, edges, visited, sheep + 1, wolf)
            else:
                dfs(info, edges, visited, sheep, wolf + 1)
            visited[v[1]] = False