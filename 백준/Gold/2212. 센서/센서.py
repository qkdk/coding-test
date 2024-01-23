import sys
import heapq

input = sys.stdin.readline

n = int(input())
k = int(input())

sensors = list(map(int, input().split()))

sensors.sort()

dist = []
for i in range(1, len(sensors)):
    heapq.heappush(dist, -(sensors[i] - sensors[i - 1]))

try:
    for _ in range(k - 1):
        heapq.heappop(dist)
except:
    print(0)
else:
    print(-sum(dist))