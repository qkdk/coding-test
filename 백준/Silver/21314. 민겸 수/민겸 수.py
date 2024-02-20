import sys

input = sys.stdin.readline

s = input().strip()

idx = -1
divLst = []
for i, v in enumerate(s):
    if v == 'K':
        divLst.append(s[idx + 1: i + 1])
        idx = i

# 가장 큰 수
maxLst = []
minLst = []
for v in divLst:
    maxLst.append(str(5 * 10 ** (len(v) - 1)))
    minLst.append(str(10 ** (len(v) - 1))[: -1] + '5')

last = s[idx + 1:]
if len(last) > 0:
    maxLst.append('1' * len(last))
    minLst.append(str(max(10 ** (len(last) - 1), 1)))

print(''.join(maxLst))
print(''.join(minLst))