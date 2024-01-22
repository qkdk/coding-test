import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
x = int(input())
lst.sort()

leftPoint = 0
rightPoint = len(lst) - 1

answer = 0
while leftPoint != rightPoint:
    curValue = lst[leftPoint] + lst[rightPoint]

    if curValue == x:
        answer += 1
        leftPoint += 1
    elif curValue < x:
        leftPoint += 1
    elif curValue > x:
        rightPoint -= 1

print(answer)