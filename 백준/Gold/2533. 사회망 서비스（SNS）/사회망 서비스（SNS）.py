import sys

sys.setrecursionlimit(1000001)

input = sys.stdin.readline

n = int(input())
tree = {}
for i in range(1, n + 1):
    tree[i] = []

dp = [[0] * (n + 1) for _ in range(2)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)


# 트리의 끝으로 내려가서 자기가 얼리어답터 인경우, 얼리어답터가 아닌경우 필요한 얼리어답터 수 최신화
# 맨 마지막은 얼리어답터인경우 1, 아닌경우 0
def makeDp(tree, start, dp, visited):
    nexts = tree[start]

    for next in nexts:
        if not visited[next]:
            visited[next] = True
            makeDp(tree, next, dp, visited)

    if not nexts:
        dp[0][start] = 1
        dp[1][start] = 0
    else:
        dp[0][start] = 1
        for next in nexts:
            # 자기가 얼리어답터인 경우
            dp[0][start] += min(dp[1][next], dp[0][next])
            # 자기가 얼리어답터가 아닌 경우
            dp[1][start] += dp[0][next]


visited[1] = True
makeDp(tree, 1, dp, visited)
print(min(dp[0][1], dp[1][1]))
# print(dp)