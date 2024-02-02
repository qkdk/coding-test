import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
beltQ = deque(list(map(int, input().split())))
robotQ = deque([False] * (n * 2))
answer = 1


def robotUp():
    if beltQ[0] != 0:
        beltQ[0] -= 1
        robotQ[0] = True


def moveBelt():
    robotQ.appendleft(robotQ.pop())
    beltQ.appendleft(beltQ.pop())


def moveRobot():
    for i in range(n - 2, -1, -1):
        if robotQ[i] == True and robotQ[i + 1] == False and beltQ[i + 1] != 0:
            robotQ[i] = False
            robotQ[i + 1] = True
            beltQ[i + 1] -= 1


def checkEnd():
    global answer

    count = 0
    for v in beltQ:
        if v == 0:
            count += 1

    if count >= k:
        print(answer)
        exit()
    answer += 1


def checkDown():
    if robotQ[n - 1] == True:
        robotQ[n - 1] = False


def solve():
    while True:
        moveBelt()
        checkDown()
        moveRobot()
        checkDown()
        robotUp()
        checkEnd()


solve()