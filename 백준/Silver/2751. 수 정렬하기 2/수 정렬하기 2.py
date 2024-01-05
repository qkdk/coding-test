import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

while q:
    print(heapq.heappop(q))