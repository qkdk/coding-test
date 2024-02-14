import sys, heapq, math

input = sys.stdin.readline

n, h, t = map(int, input().split())
q = []
for _ in range(n):
    heapq.heappush(q, -int(input()))


def solve():
    i = 0
    while i < t:
        if -q[0] == 1:
            break

        if -q[0] < h:
            break

        pop = heapq.heappop(q)
        heapq.heappush(q, math.ceil(pop / 2))
        i += 1

    if -min(q) < h:
        print("YES")
        print(i)
    else:
        print("NO")
        print(-min(q))


solve()