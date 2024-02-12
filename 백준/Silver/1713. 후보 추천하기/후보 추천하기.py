import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int, input().strip().split(" ")))

CT = 0
SN = 1

answer = []


def delete():
    target = answer[0]
    minValue = float('inf')
    for v in answer:
        if minValue > v[CT]:
            minValue = v[CT]
            target = v

    answer.remove(target)


for j, v in enumerate(lst):
    for i in range(len(answer)):
        if answer[i][SN] == v:
            answer[i][CT] += 1
            break
    else:
        if len(answer) == n:
            delete()
        answer.append([1, v])

answer.sort(key=lambda x: x[SN])
for v in answer:
    print(v[SN], end=' ')