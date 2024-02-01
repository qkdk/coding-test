import sys

input = sys.stdin.readline


def solve():
    numbers = [
        {(1, 1), (2, 1), (3, 1)}
        , {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1)}
        , {(1, 0), (1, 1), (3, 1), (3, 2)}
        , {(1, 0), (1, 1), (3, 0), (3, 1)}
        , {(0, 1), (1, 1), (3, 0), (4, 0), (3, 1), (4, 1)}
        , {(1, 1), (1, 2), (3, 0), (3, 1)}
        , {(1, 1), (1, 2), (3, 1)}
        , {(1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1)}
        , {(1, 1), (3, 1)}
        , {(1, 1), (3, 0), (3, 1)}
    ]

    n, table = consoleInput()
    zeroIndexes = scanNumber(table)
    nums = [0 for _ in range(n)]
    counts = [0 for _ in range(n)]

    for j, numSet in enumerate(zeroIndexes):
        for i, vSet in enumerate(numbers):
            if not vSet - numSet:
                nums[j] += i * 10 ** (n - 1 - j)
                counts[j] += 1

    totalCount = 1
    answer = 0
    for i in range(n):
        tmpCount = 1
        for j in range(n):
            if i != j:
                tmpCount *= counts[j]
            if i == 0:
                totalCount *= counts[j]
        answer += nums[i] * tmpCount

    if totalCount == 0:
        return -1
    return answer / totalCount

def scanNumber(table):
    nums = []
    idx = 0
    while idx < len(table[0]):
        tmpSet = set()
        for i in range(5):
            for j in range(3):
                if table[i][j + idx] == '.':
                    tmpSet.add((i, j))

        idx += 4
        nums.append(tmpSet)
    return nums


def consoleInput():
    n = int(input())
    table = []
    for _ in range(5):
        table.append(list(input().strip()))
    return n, table


print(solve())