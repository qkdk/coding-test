import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

lst.sort()


def solve():
    minValue = float('inf')
    answer = []

    for k in range(len(lst) - 2):
        left = k + 1
        right = len(lst) - 1

        while left != right:
            tmpSum = lst[left] + lst[right] + lst[k]
            if minValue > abs(tmpSum):
                minValue = abs(tmpSum)
                answer = [lst[left], lst[right], lst[k]]

            if tmpSum == 0:
                return map(str, sorted(answer))
            elif tmpSum < 0:
                left += 1
            else:
                right -= 1

    return map(str, sorted(answer))


print(' '.join(solve()))