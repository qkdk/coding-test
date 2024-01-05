import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())

q = PriorityQueue()
for _ in range(n):
    q.put(int(input()))

for _ in range(n):
    print(q.get())