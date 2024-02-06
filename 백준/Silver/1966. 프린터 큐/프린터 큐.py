import sys
from collections import deque

input = sys.stdin.readline


def solve():
    tc = int(input())
    for _ in range(tc):
        n, m = map(int, input().split())
        lst = list(map(int, input().split()))
        q = deque()

        for i, v in enumerate(lst):
            q.append((i, v))

        INDEX = 0
        VALUE = 1
        answer = 0
        while q:
            answer += 1
            cur = q.popleft()

            for v in q:
                if v[VALUE] > cur[VALUE]:
                    q.append(cur)
                    answer -= 1
                    break
            else:
                if cur[INDEX] == m:
                    print(answer)
                    q.clear()


solve()