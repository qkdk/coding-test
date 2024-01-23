import sys
import heapq

END = 1
START = 0

input = sys.stdin.readline

n = int(input())

times = []
for _ in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort(key=lambda x: x[START])

q = []
heapq.heappush(q, (times[0][END], times[0][START]))

HEAPSTART = 1
HEAPEND = 0

answer = 1
for v in times[1:]:
    if q[0][HEAPEND] <= v[START]:
        heapq.heappop(q)
    else:
        answer += 1
    heapq.heappush(q, (v[END], v[START]))

print(answer)