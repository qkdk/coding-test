import sys
from collections import deque, Counter

input = sys.stdin.readline

s = list(map(int, input().strip()))
counter = Counter(s)

zero = counter[0] / 2
one = counter[1] / 2

q = deque()

for v in s:
    if v == 1 and one > 0:
        one -= 1
        continue
    q.append(v)

answer = deque()
for i in range(len(q) - 1, -1, -1):
    if q[i] == 0 and zero > 0:
        zero -= 1
        continue
    answer.appendleft(str(q[i]))

print(''.join(answer))