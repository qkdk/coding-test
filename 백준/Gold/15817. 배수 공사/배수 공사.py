# 중복을 제거해서 배낭문제를 푸는것이 어렵, 왼쪽부터가 아닌 오른쪽 부터 탐색

import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

dp = [0] * (m + 1)
dp[0] = 1

for _ in range(n):
    l, c = map(int, input().strip().split())

    for i in range(len(dp) - 1, -1, -1):
        for j in range(1, c + 1):
            val = l * j
            if i >= val:
                dp[i] += dp[i - val]
            else:
                break

print(dp[-1])