import sys

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    lst = list(map(int, input().strip().split()))
    rightMaxLst = [0] * len(lst)

    maxValue = 0
    for i in range(len(lst) - 1, - 1, -1):
        maxValue = max(maxValue, lst[i])
        rightMaxLst[i] = maxValue

    answer = 0
    for i in range(len(lst)):
        answer += rightMaxLst[i] - lst[i]

    print(answer)