import sys

input = sys.stdin.readline

inputLst = list(map(int, input().strip()))

inputLst.sort(reverse=True)
for v in inputLst:
    print(v, end='')