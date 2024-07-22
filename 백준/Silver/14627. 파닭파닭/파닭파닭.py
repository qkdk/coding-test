import sys

input = sys.stdin.readline

S, C = map(int, input().strip().split())
arr = []
for _ in range(S):
    arr.append(int(input()))

li = 1
ri = max(arr)
mid = 0

while ri >= li:
    mid = (li + ri) // 2
    count = 0
    for v in arr:
        count += (v // mid)

    if count >= C:
        li = mid + 1
    else:
        ri = mid - 1

# print(ri)
print(sum(arr) - (ri * C))