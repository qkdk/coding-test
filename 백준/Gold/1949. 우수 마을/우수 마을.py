import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

n = int(input())

people = [0]

for v in map(int, input().strip().split()):
    people.append(v)

tree = {}
for i in range(1, n + 1):
    tree[i] = []
for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0] * (n + 1) for _ in range(2)]
visited = [False] * (n + 1)
visited[1] = True


def dfs(start, tree, visited, dp, people):
    # 말단까지 이동
    nexts = tree.get(start)

    dp[0][start] = people[start]

    for next in nexts:
        if visited[next]:
            continue
        visited[next] = True
        dfs(next, tree, visited, dp, people)
        dp[0][start] += dp[1][next]
        dp[1][start] += max(dp[0][next], dp[1][next])


dfs(1, tree, visited, dp, people)
print(max(dp[0][1], dp[1][1]))