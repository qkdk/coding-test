import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

lst = list(map(int, input().strip().split()))

lst.sort()

answer = []


def dfs(index, lst, curDepth, maxDepth, result):
    if curDepth == maxDepth:
        answer.append(result.copy())
        return

    for i in range(index, len(lst)):
        result[curDepth] = lst[i]
        dfs(i + 1, lst, curDepth + 1, maxDepth, result)


dfs(0, lst, 0, m, [0] * m)

a = ""
for v in answer:
    a += ' '.join(map(str, v))
    a += "\n"

print(a)