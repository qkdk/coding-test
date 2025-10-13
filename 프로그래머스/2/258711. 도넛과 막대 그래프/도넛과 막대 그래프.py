def solution(edges):
    answer = [0,0,0,0]
    
    in_count = [0] * 1000001
    out_count = [0] * 1000001
    
    for i, o in edges:
        in_count[o] += 1
        out_count[i] += 1
        
    for i in range(1, len(in_count)):
        if in_count[i] == 0 and out_count[i] >= 2:
            answer[0] = i
        if in_count[i] >= 1 and out_count[i] == 0:
            answer[2] += 1
        if in_count[i] >= 2 and out_count[i] == 2:
            answer[3] += 1
        
    answer[1] = out_count[answer[0]] - answer[2] - answer[3]
        
    
    return answer
# 기존 풀이
# def solution(edges):
#     # graph 그리기
#     graph = {}
#     max_node = 0
#     for start, end in edges:
        
#         max_node = max(max(start, end), max_node)
        
#         if start not in graph:
#             graph[start] = []
#         graph[start].append(end)
    
    
#     # 시작 노드 찾기
#     start_visited = [False] * (max_node + 1)
#     for i, vs in graph.items():
#         for v in vs:
#             start_visited[v] = True
    
#     start_node = 0
#     for i in range(1, len(start_visited), 1):
#         if start_visited[i] == False:
#             if len(graph[i]) >= 2:
#                 start_node = i
    
#     for i in range(1, max_node + 1, 1):
#         if i not in graph:
#             graph[i] = []
            
#     answer = [0]  * 4
    
#     for next in graph[start_node]:
#         visited = [False] * (max_node + 1)
#         visited[next] = True
#         e, n = dfs(graph, next, visited)
#         # print(e, n)
#         if e == n:
#             answer[1] += 1
#         elif e == n - 1:
#             answer[2] += 1
#         elif e == n + 1:
#             answer[3] += 1
            
#     answer[0] = start_node
#     return answer

# def dfs(graph, n, visited):
    
#     # visited[n] = True
#     node_count = 1
#     edge_count = 0
    
#     for next in graph[n]:
#         if visited[next]:
#             edge_count += 1
#         else:
#             visited[next] = True
#             r_edge_count, r_node_count = dfs(graph, next, visited)
#             edge_count += r_edge_count
#             node_count += r_node_count
#             edge_count += 1
        
#     return edge_count, node_count
    
    