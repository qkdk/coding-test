import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []

for v in list(map(int, input().split())):
    heapq.heappush(q, v)

for _ in range(1, n):
    for v in list(map(int, input().split())):
        heapq.heappush(q, v)
        heapq.heappop(q)

print(heapq.heappop(q))