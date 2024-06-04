import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

dic = {}

for i in range(1, n + 1):
    dic[i] = set()

target = 0
for _ in range(m):
    lst = list(map(int, input().strip().split()))
    tmp = lst[1:]
    tmp.sort()

    if tmp[0] == 1:
        count = len(tmp) - 1
        for v in tmp:
            for i in range(count):
                dic[v].add(target + i)

        target += count
    else:
        t = set()
        for v in tmp:
            t = t.union(dic[v])

        for v in tmp:
            dic[v] = dic[v].union(t)

for v in dic:
    if len(dic[v]) == target:
        print(v)