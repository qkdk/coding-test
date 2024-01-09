import sys

input = sys.stdin.readline

a = input().strip().split("-")

tmpLst = []
for v in a:
    tmpLst.append(sum(map(int, v.split("+"))))

answer = tmpLst[0]
for i in range(1,len(tmpLst)):
    answer -= tmpLst[i]

print(answer)