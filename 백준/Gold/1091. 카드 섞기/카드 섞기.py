import sys

input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().split()))
pri = list(map(int, input().split()))


def check(cards):
    for i, v in enumerate(cards):
        if i % 3 != v:
            return False
    return True


s = set()


def duplicateCheck(cards):
    tmpStr = ''.join(map(str, cards))
    if tmpStr in s:
        return True

    s.add(tmpStr)
    return False


def solve(cards):
    tmpCards = [0] * n
    answer = 0
    while True:
        if duplicateCheck(cards):
            return -1
        if check(cards):
            return answer
        for i, v in enumerate(pri):
            tmpCards[v] = cards[i]
        cards = tmpCards[::]
        answer += 1


print(solve(cards))