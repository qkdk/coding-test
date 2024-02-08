import sys

input = sys.stdin.readline

lst = list(input().strip())
stack = [[0, 0]]
for v in lst:
    if stack:
        if v == '(':
            stack.append(['(', 0])
        elif v == ')':
            if stack[-1][0] == '(':
                pop = stack.pop()
                tmpValue = 0
                if pop[1] == 0:
                    tmpValue = 2
                else:
                    tmpValue = 2 * pop[1]
                stack[-1][1] += tmpValue
            else:
                stack.append([')', 0])

        elif v == '[':
            stack.append(['[', 0])

        elif v == ']':
            if stack[-1][0] == '[':
                pop = stack.pop()
                tmpValue = 0
                if pop[1] == 0:
                    tmpValue = 3
                else:
                    tmpValue = 3 * pop[1]
                stack[-1][1] += tmpValue
            else:
                stack.append([']', 0])
    else:
        stack.append([v, 0])

if len(stack) == 1:
    print(stack[0][1])
else:
    print(0)