import sys

input = sys.stdin.readline

tmpSet = set()

line = input().strip()

for i in range(len(line) + 1):
    for j in range(i + 1, len(line) + 1):
        tmpSet.add(line[i:j])

print(len(tmpSet))