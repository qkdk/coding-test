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