import sys, heapq

input = sys.stdin.readline

n, m, k = map(int, input().strip().split())

lst = []
for _ in range(k):
    lst.append(tuple(map(int, input().strip().split())))


def solve():
    lst.sort(key=lambda x: x[1])
    q = []

    summ = 0

    for v in lst:
        heapq.heappush(q, v)

        summ += v[0]

        if len(q) == n:
            if summ >= m:
                return v[1]
            else:
                pop = heapq.heappop(q)
                summ -= pop[0]

    return -1


print(solve())