import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().strip().split()))


def findAB(x0, x1, x2):
    a = 0.0
    if x1 - x0 != 0:
        a = (x2 - x1) / (x1 - x0)
    b = x2 - x1 * a

    return a, b


def solve():
    if n < 2:
        return "A"
    if n == 2:
        if lst[0] == lst[1]:
            return lst[0]
        else:
            return "A"

    a, b = findAB(lst[0], lst[1], lst[2])

    if not a.is_integer() or not b.is_integer():
        return "B"

    for i in range(1, len(lst)):
        if lst[i - 1] * a + b != lst[i]:
            return "B"

    return int(lst[-1] * a + b)


print(solve())