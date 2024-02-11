import sys

input = sys.stdin.readline

a, b, n = map(int, input().split())

bStack = []
rStack = []

for _ in range(n):
    t, c, m = input().strip().split()
    t = int(t)
    m = int(m)
    if c == "B":
        st = t
        if bStack:
            st = max(bStack[-1][0] + a, t)
        for i in range(m):
            bStack.append((st + i * a, 0))
    else:
        st = t
        if rStack:
            st = max(rStack[-1][0] + b, t)
        for i in range(m):
            rStack.append((st + i * b, 1))

bStack.extend(rStack)

bStack.sort()

count = 1
bbStack = []
rrStack = []
for v in bStack:
    if v[1] == 0:
        bbStack.append(str(count))
        count += 1
    else:
        rrStack.append(str(count))
        count += 1

print(len(bbStack))
print(' '.join(bbStack))
print(len(rrStack))
print(' '.join(rrStack))