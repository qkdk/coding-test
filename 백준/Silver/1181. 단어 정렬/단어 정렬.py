import sys

input = sys.stdin.readline

n = int(input())

lst = set()
# list = []
for _ in range(n):
    # list.append()
    lst.add(input().rstrip())
lst = list(lst)
lst.sort(key=lambda x: (len(x), x))

for v in lst:
    print(v)