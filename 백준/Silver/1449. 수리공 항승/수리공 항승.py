import sys

input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
end = lst[0] + l

answer = 1
for v in lst[1:]:
    if v >= end:
        end = v + l
        answer += 1

print(answer)