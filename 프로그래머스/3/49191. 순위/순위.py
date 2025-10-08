def solution(n, results):
    
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    for winner, looser in results:
        graph[winner][looser] = 1
        graph[looser][winner] = -1
    
    for k in range(1, n + 1, 1):
        for i in range(1, n + 1, 1):
            for j in range(1, n + 1, 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    
    answer = 0
    
    for row in graph:
        count = 0
        for i in range(len(row)):
            if row[i] == 0:
                count += 1
        if count == 2:
            answer += 1
            
    return answer

def print_matrix(matrix):
    for row in matrix:
        print(row)