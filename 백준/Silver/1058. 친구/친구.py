n = int(input())

graph = {i: [] for i in range(1, n + 1)}
visited = {i: [False] * (n + 1) for i in range(1, n + 1)}

for i in range(1, n + 1):
    for j, v in enumerate(list(input())):
        if v == "Y":
            graph[i].append(j + 1)

answer = 0

for k, v in graph.items():
    for e in v:
        visited[k][e] = True
        for d in graph[e]:
            if k != d and not visited[k][d]:
                visited[k][d] = True

    answer = max(answer, sum(visited[k]))

print(answer)