import sys
INF = int(1e9)

input = sys.stdin.readline

n = int(input())

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    tmpLst = list(map(int, input().split()))
    for j in range(n):
        # if i == j:
        #     dist[i][j] = 0
        if tmpLst[j] == 1:
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

for row in dist:
    for v in row:
        if v != INF:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()