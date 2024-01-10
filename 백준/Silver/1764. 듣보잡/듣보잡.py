import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lSet = set()
for _ in range(n):
    lSet.add(input().strip())

answer = []
answerCount = 0
for _ in range(m):
    tmpInput = input().strip()
    if tmpInput in lSet:
        answerCount += 1
        answer.append(tmpInput)

answer.sort()
print(answerCount)
print('\n'.join(answer))