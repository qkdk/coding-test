import re, sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    line = input().strip()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(line):
        print("YES")
    else:
        print("NO")