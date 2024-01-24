import sys
import bisect

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
# 3가지로 분리 0 이하/1/2이상
left = bisect.bisect_left(lst, 1)
mLst = lst[:left]
right = bisect.bisect_right(lst, 1)
pLst = lst[right:]

answer = right - left
def mult(lst):
    answer = 0
    for i in range(1, len(lst), 2):
        answer += lst[i - 1] * lst[i]
    if len(lst) % 2 == 1:
        answer += lst[-1]

    return answer

answer += mult(mLst)
pLst.sort(reverse=True)
answer += mult(pLst)

print(answer)