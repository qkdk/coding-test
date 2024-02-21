import sys

input = sys.stdin.readline

n = int(input())

mTmp = list(map(int, input().strip().split()))
wTmp = list(map(int, input().strip().split()))


def extract(lst: list):
    result = []
    i = 0
    for i, v in enumerate(lst):
        if v > 0:
            result.append(lst[0:i])
            result.append(lst[i:])
            break
    else:
        result.append(lst)
        result.append([])
    return result, i


def solve():
    mTmp.sort()
    wTmp.sort()

    m, mi = extract(mTmp)
    w, wi = extract(wTmp)

    answer = 0

    idx = len(w[1]) - 1
    for v in m[0]:
        for j in range(idx, -1, -1):
            if v + w[1][j] < 0:
                answer += 1
                idx -= 1
                break
            else:
                idx -= 1

    idx = len(w[0]) - 1
    for v in m[1]:
        for j in range(idx, -1, -1):
            if v + w[0][j] < 0:
                answer += 1
                idx -= 1
                break
            else:
                idx -= 1

    return answer


print(solve())