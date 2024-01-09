import sys
from collections import Counter

input = sys.stdin.readline

inputStr = input().strip()
upper = inputStr.upper()
counter = Counter(upper)

maxCount = 1
maxValue = 0
answer = ''
for k, v in counter.items():
    if maxValue < v:
        maxValue = v
        maxCount = 1
        answer = k
    elif maxValue == v:
        maxCount += 1

if maxCount != 1:
    print("?")
else:
    print(answer)