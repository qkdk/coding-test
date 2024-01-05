import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    x, y = map(int, input().split())

    heapq.heappush(q, (x,y, f'{x} {y}'))

while q:
    print(heapq.heappop(q)[2])