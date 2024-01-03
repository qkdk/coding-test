a, b = map(int, input().split())

def dfs(target, value, depth):

    if value == 0:
        return -1
    if target == value:
        return depth
    if value % 2 == 0:
        return dfs(target, int(value / 2), depth + 1)
    elif str(value)[-1] == "1":
        return dfs(target, int(value / 10), depth + 1)
    else:
        return -1

print(dfs(a, b,1))