import sys

input = sys.stdin.readline


def solve():
    n, s, p = map(int, input().split())
    if n == 0:
        return 1
    lst = list(map(int, input().split()))

    idx = 0
    for i in range(len(lst)):
        if lst[i] < s:
            idx = i
            lst.insert(i, s)
            break
    else:
        idx = len(lst)
        lst.append(s)

    if idx >= p:
        return -1
    
    prize = 1
    for i in range(len(lst[: idx + 1])):
        if i == 0:
            prize = 1
        elif lst[i] != lst[i - 1]:
            prize = i + 1
    return prize

print(solve())