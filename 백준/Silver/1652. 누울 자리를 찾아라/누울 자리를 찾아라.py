import sys,copy

input = sys.stdin.readline

n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

rCount = 0
cCount = 0

rVisited = [[False] * n for _ in range(n)]
cVisited = copy.deepcopy(rVisited)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '.' and rVisited[i][j] == False:
            tmpCount = 0
            for k in range(j, n):
                if matrix[i][k] == '.':
                    rVisited[i][k] = True
                    tmpCount += 1
                else:
                    break
            if tmpCount >= 2:
                rCount += 1

for i in range(n):
    for j in range(n):
        if matrix[j][i] == '.' and cVisited[j][i] == False:
            tmpCount = 0
            for k in range(j, n):
                if matrix[k][i] == '.':
                    cVisited[k][i] = True
                    tmpCount += 1
                else:
                    break
            if tmpCount >= 2:
                cCount += 1

print(rCount, cCount)