import sys

input = sys.stdin.readline

tc = int(input())


def makeAnswer(ex):
    lst = []
    lst.append(ex[0])

    for i in range(1, len(ex)):
        if lst[-1].isdigit() and ex[i].isdigit():
            lst.append(" ")
        lst.append(ex[i])

    answer.append(''.join(lst))


def dfs(ex, cur, n):
    if cur > n:
        if eval(ex) == 0:
            makeAnswer(ex)
        return

    dfs(ex + "+" + str(cur), cur + 1, n)
    dfs(ex + "-" + str(cur), cur + 1, n)
    dfs(ex + str(cur), cur + 1, n)


for _ in range(tc):
    n = int(input())
    answer = []
    dfs("1", 2, n)
    answer.sort()
    for v in answer:
        print(v)
    print()