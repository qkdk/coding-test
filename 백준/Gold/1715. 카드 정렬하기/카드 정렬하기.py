import sys, heapq

input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

answer = 0
while len(q) != 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)

    tmp = first + second
    answer += tmp
    heapq.heappush(q, tmp)

print(answer)