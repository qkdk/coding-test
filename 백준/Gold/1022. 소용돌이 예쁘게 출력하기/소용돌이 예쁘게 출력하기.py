import sys

input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

matrix = []


def findNumber(y, x):
    if y < x:
        n = max(abs(y), abs(x))
        a = 4 * n * n - 2 * n
        return a - (x + y) + 1
    else:
        n = max(abs(y), abs(x))
        a = 4 * n * n + 2 * n
        return a + (x + y) + 1


for y in range(r2 - r1 + 1):
    tmpLst = []
    for x in range(c2 - c1 + 1):
        tmpLst.append(findNumber(y + r1, x + c1))
    matrix.append(tmpLst)

maxValue = 0
for row in matrix:
    for v in row:
        maxValue = max(maxValue, v)

maxLength = len(str(maxValue))

for row in matrix:
    for v in row:
        print(str(v).rjust(maxLength, " "), end=" ")
    print()