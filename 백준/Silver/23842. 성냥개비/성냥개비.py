import sys

input = sys.stdin.readline


dic = {}
dic[0] = 6
dic[1] = 2
dic[2] = 5
dic[3] = 5
dic[4] = 4
dic[5] = 5
dic[6] = 6
dic[7] = 3
dic[8] = 7
dic[9] = 6

answer = ""
def solve(n):
    dfs(0, 6, [0] * 6, n - 4)
    print("impossible")
    return

def dfs(curDepth, maxDepth, result, count):
    if count < 0:
        return
    
    if curDepth == maxDepth:
        if count == 0:
            if result[0] * 10 + result[1] + result[2] * 10 + result[3] == result[4] * 10 + result[5]:
                print(str(result[0]) + str(result[1]) + "+" + str(result[2]) + str(result[3]) + "=" + str(result[4]) + str(result[5]))
                sys.exit()
        return

    for i in range(10):
        result[curDepth] = i
        dfs(curDepth + 1, maxDepth, result, count - dic[i])


n = int(input())

solve(n)