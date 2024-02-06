import sys, math

input = sys.stdin.readline

n, m, b = map(int, input().split())
heightCount = [0 for _ in range(257)]

for _ in range(n):
    for v in map(int, input().split()):
        heightCount[v] += 1


def solve():
    maxHeight = 0
    cost = float('inf')

    for targetHeight in range(257):
        digCount = 0
        adCount = 0

        for currentHeight in range(257):
            if targetHeight > currentHeight:
                adCount += heightCount[currentHeight] * (targetHeight - currentHeight)
            elif currentHeight > targetHeight:
                digCount += heightCount[currentHeight] * (currentHeight - targetHeight)

        # 평탄화에 성공하는 경우
        if digCount + b >= adCount:
            nCost = digCount * 2 + adCount
            if cost >= nCost:
                cost = nCost
                maxHeight = targetHeight

    return cost, maxHeight


a, b = solve()
print(a, b)