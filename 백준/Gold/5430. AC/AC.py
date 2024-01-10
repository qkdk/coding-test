import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    cmd = input().strip()
    length = int(input())
    tmpLst = input().strip()[1:-1].split(",")

    leftStart = True

    q = deque()
    if length != 0:
        q = deque(tmpLst)

    for v in cmd:
        if v == "R":
            leftStart = not leftStart
        else:
            if q:
                if leftStart:
                    q.popleft()
                else:
                    q.pop()
            else:
                print("error")
                break
    else:
        if not leftStart:
            q.reverse()
        print("[" + ','.join(q) + "]")