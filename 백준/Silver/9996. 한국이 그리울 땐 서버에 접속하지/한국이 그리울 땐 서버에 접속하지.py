import sys, re

input = sys.stdin.readline

n = int(input())
line = input().strip()
split = line.split("*")
regex = ".*".join(split)
p = re.compile(regex)

for _ in range(n):
    if p.fullmatch(input().strip()):
        print("DA")
    else:
        print("NE")