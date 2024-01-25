import sys

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(input().strip())

def calculateNumber(x):
    num = 0

    for v in x:
        if str.isdigit(v):
            num += int(v)

    return num

lst.sort(key=lambda x: (len(x), calculateNumber(x),x))

for v in lst:
    print(v)