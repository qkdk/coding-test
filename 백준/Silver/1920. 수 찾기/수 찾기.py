import sys
import bisect

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
inp = list(map(int, input().split()))

for v in inp:
    index = bisect.bisect_left(lst, v)
    if index == len(lst):
        print(0)
    elif lst[index] != v:
        print(0)
    else:
        print(1)