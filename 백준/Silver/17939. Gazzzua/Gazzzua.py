# 다음에 내릴때만 파는게 아니라
# 가장 큰값에 다 팔아야 한다.

# 꺼꾸로 배열을 탐색하면서 뒤에 있는 최대값을 적어준다

import sys

input = sys.stdin.readline

n = int(input())
chart = list(map(int, input().strip().split()))
dp = [0] * (len(chart) + 1)

for i in range(len(chart) - 1, -1, -1):
    dp[i] = max(dp[i + 1], chart[i])

count = 0
money = 0
for i in range(len(chart)):
    if chart[i] < dp[i]:
        count += 1
        money -= chart[i]

    else:
        money += chart[i] * count
        count = 0

print(money)