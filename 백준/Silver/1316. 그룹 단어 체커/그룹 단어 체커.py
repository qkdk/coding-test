import sys

input = sys.stdin.readline

n = int(input())

answer = 0
for _ in range(n):
    inputStr = input().strip()
    prevChar = ''
    tmpSet = set()
    for v in inputStr:
        if prevChar != v:
            if v in tmpSet:
                break
        prevChar = v
        tmpSet.add(v)
    else:
        answer += 1

print(answer)