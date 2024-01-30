import sys, re

input = sys.stdin.readline
line = input().strip()
p = re.compile('(100+1+|01)+')

if p.fullmatch(line):
    print("SUBMARINE")
else:
    print("NOISE")