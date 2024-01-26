import sys
import heapq

input = sys.stdin.readline

n = int(input())

ROOM = 0
START = 1
END = 2
QSTART = 1
QEND = 0

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: x[START])

q = []

# 종료시점 기준으로 정렬
heapq.heappush(q, (lst[0][END], lst[0][START]))

answer = 1
for v in lst[1:]:
    if q[0][QEND] <= v[START]:
        heapq.heappop(q)
        heapq.heappush(q, (v[END], v[START]))
    else:
        answer += 1
        heapq.heappush(q, (v[END], v[START]))

print(answer)