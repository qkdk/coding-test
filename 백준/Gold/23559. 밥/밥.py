import sys, heapq

input = sys.stdin.readline

n, x = map(int, input().strip().split())

q = []
lst = []
costSum = 0
answer = 0
# 가격이 높고 밸류가 낮은게 우선순위 높다.
for i in range(n):
    a, b = map(int, input().strip().split())
    lst.append(b - a)
    heapq.heappush(q, (b - a, i))
    answer += b
    costSum += 1000

while True:
    if costSum + 4000 <= x:
        heappop = heapq.heappop(q)
        if heappop[0] > 0:
            break
        costSum += 4000
        answer -= lst[heappop[1]]

    else:
        break

print(answer)