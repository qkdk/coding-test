import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = []
for _ in range(m):
    a = int(input())
    lst.append(a)

lst.sort()

answer = 0
t = 0
for i, v in enumerate(lst):
    vv = v * (min(len(lst) - i, n))

    if vv > answer:
        t = v
        answer = vv

print(t, answer)