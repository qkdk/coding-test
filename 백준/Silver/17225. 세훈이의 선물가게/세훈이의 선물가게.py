import sys
from collections import deque

input = sys.stdin.readline

a, b, n = map(int, input().split())

bq = deque()
rq = deque()

aStack = []
bStack = []

for _ in range(n):
    t, c, m = input().strip().split()
    t = int(t)
    m = int(m)
    if c == "B":
        for i in range(m):
            bq.append(t + i * a)
    else:
        for i in range(m):
            rq.append(t + i * b)

count = 1
second = 1
while second < 86401:
    if bq and bq[0] < second:
        bq.popleft()
        aStack.append(count)
        count += 1
    elif rq and rq[0] < second:
        rq.popleft()
        bStack.append(count)
        count += 1
    else:
        second += 1

print(len(aStack))
print(' '.join(map(str, aStack)))
print(len(bStack))
print(' '.join(map(str, bStack)))