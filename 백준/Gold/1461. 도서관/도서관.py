import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()


# 0의 위치 찾기
def findP():
    for i, v in enumerate(lst):
        if v >= 0:
            return i
    return len(lst)


answer = 0
if abs(lst[0]) > abs(lst[-1]):
    answer -= abs(lst[0])
else:
    answer -= lst[-1]

# 음수
ns = findP() - 1
ns -= ns % m
while ns >= 0:
    answer += abs(lst[ns]) * 2
    ns -= m

# 양수
ps = findP()
ps += (len(lst) - ps - 1) % m
while ps < len(lst):
    answer += abs(lst[ps]) * 2
    ps += m

print(answer)