import sys

input = sys.stdin.readline

lst = list(input().strip())


def solve():
    stack = []
    for v in lst:
        stack.append(v)

        if len(stack) >= 4:
            if stack[-1] == 'P' and stack[-2] == 'A' and stack[-3] == 'P' and stack[-4] == 'P':
                for _ in range(4):
                    stack.pop()
                stack.append('P')

    if len(stack) == 1:
        if stack[0] == 'P':
            return 'PPAP'

    return 'NP'


print(solve())