import sys

MAX = float('inf')

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int, input().split())
        lst.append((a, b))
    lst.sort(key=lambda x: x[0])

    answer = [lst[0]]
    for score in lst[1:]:
        s = score[1]

        if s < answer[-1][1]:
            answer.append(score)

    print(len(answer))