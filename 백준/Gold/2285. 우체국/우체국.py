import sys

input = sys.stdin.readline

n = int(input())
dic = {}
count = 0

for _ in range(n):
    a, b = map(int, input().split())
    count += b
    dic[a] = b


def solve():
    mid = count // 2
    tmp = sorted(dic.items(), key=lambda x: x[0])
    t = 0
    for v in tmp:
        t += v[1]
        if t > mid:
            return v[0]


print(solve())