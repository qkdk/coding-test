import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().strip().split()))

def solve():
    if n == 1:
        return sum(lst) - max(lst)

    minLst = []
    minLst.append(min(lst[0], lst[5]))
    minLst.append(min(lst[1], lst[4]))
    minLst.append(min(lst[2], lst[3]))
    minLst.sort()

    min1 = min(minLst)
    min2 = minLst[0] + minLst[1]
    min3 = sum(minLst)

    answer = 0
    answer += 4 * min3
    answer += (8 * n - 12) * min2
    answer += (5 * n * n - 16 * n + 12) * min1

    return answer

print(solve())
