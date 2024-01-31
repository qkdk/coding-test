import sys

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(input().strip())

answer = 0
for i in range(n):
    v = input().strip()

    if v != lst[i]:
        lst.remove(v)
        lst.insert(i, v)
        answer += 1

print(answer)