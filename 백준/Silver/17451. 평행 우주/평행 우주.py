import sys

input = sys.stdin.readline


def solve(n, lst):
    lst = lst[::-1]

    prev = lst[0]
    # 역순으로 돌면서, 최대값 갱신,
    # 기존값 보다 크다면 그값 그대로
    # 작고, 기존값이랑 배수 관계면 그대로, 배수관계 아니면 큰 수중에서 배수되는 놈으로

    for i, v in enumerate(lst[1:]):
        if prev < v:
            prev = v
        else:
            if prev % v == 0:
                pass
            else:
                a = prev // v
                prev = v * (a + 1)

    return prev


n = int(input())
lst = list(map(int, input().strip().split()))

print(solve(n, lst))