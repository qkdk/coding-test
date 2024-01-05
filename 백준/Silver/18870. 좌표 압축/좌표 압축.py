import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

map = {}
for v in lst:
    map[v] = 0

sorted_map = sorted(map.items())

newCoord = 0
for v in sorted_map:
    map[v[0]] = newCoord
    newCoord += 1

answer = ""
for v in lst:
    print(map[v], end=' ')