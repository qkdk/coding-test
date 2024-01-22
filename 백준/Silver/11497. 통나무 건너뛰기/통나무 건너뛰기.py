import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    q = deque()
    for i, v in enumerate(lst):
        if i % 2 == 1:
            q.appendleft(v)
        else:
            q.append(v)

    aLst = list(q)
    answer = 0
    for i, v in enumerate(aLst):
        curValue = abs(aLst[i] - aLst[(i + 1) % len(aLst)])
        if answer < curValue:
            answer = curValue

    print(answer)