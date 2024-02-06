import sys, math

input = sys.stdin.readline

n, m, b = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 파는것은 2초 쌓는것은 1초이기 때문에 완탐을 진행해야한다.
# 그리디로 하려다가 망함...
def solve():
    summ = b
    for row in matrix:
        summ += sum(row)

    limit = math.floor(summ / (n * m))

    maxHeight = 0
    cost = float('inf')
    for k in range(limit + 1):
        digCount = 0
        adCount = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] > k:
                    digCount += matrix[i][j] - k
                elif matrix[i][j] < k:
                    adCount += k - matrix[i][j]

        # 평탄화에 성공하는 경우
        if digCount + b >= adCount:
            nCost = digCount * 2 + adCount
            if cost >= nCost:
                cost = nCost
                maxHeight = k

    return cost, maxHeight

a, b = solve()
print(a, b)