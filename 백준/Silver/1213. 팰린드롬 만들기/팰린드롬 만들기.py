import sys
from collections import Counter, deque

input = sys.stdin.readline
line = input().strip()


def findOdd(items):
    for k, v in items:
        if v % 2 == 1:
            return k

    return False

def makeList(items):
    answer = []
    for item in items:
        k, v = item
        while v >= 2:
            answer.append(k)
            v -= 2

    return answer

def solve(line):
    counter = Counter(line)
    items = sorted(counter.items(), key=lambda x: x[0])
    answer = []

    if len(line) % 2 == 1:
        count = 0
        for k, v in items:
            if v % 2 == 1:
                count += 1

        if count > 1:
            return "I'm Sorry Hansoo"

        tmpAnswer = makeList(items)
        odd = findOdd(items)

        answer.extend(tmpAnswer)
        answer.append(odd)
        answer.extend(tmpAnswer[::-1])

    else:
        for k, v in items:
            if v % 2 == 1:
                return "I'm Sorry Hansoo"


        tmpAnswer = makeList(items)
        answer.extend(tmpAnswer)
        answer.extend(tmpAnswer[::-1])

    return "".join(answer)

print(solve(line))

# 짝수 -> 모든 알파벳이 짝수
# 홀수 -> 하나만 홀수고 나머지 모두 짝수