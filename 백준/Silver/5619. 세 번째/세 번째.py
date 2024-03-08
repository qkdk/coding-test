import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
answerLst = []

c = []
if n == 3:
    c = list(combinations(lst, 2))
else:
    c = list(combinations(lst[:4], 2))
    
for v in c:
    answerLst.append(int(str(v[0]) + str(v[1])))
    answerLst.append(int(str(v[1]) + str(v[0])))

tmp = sorted(answerLst)
print(tmp[2])