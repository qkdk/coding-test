import sys
import bisect

input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

c.sort(reverse=True)
b.sort()

indexes = []

for v in c:
    right = bisect.bisect_right(b, v)
    indexes.append(right - 1)

visited = [False for _ in range(len(b))]

if indexes[0] < len(b) - 1:
    print(-1)

else:
    answer = 0
    while True:
        if False not in visited:
            break

        flag = False
        answer += 1

        for i, idx in enumerate(indexes):
            if flag:
                break

            while True:
                if indexes[i] < 0:
                    flag = True
                    break
                if visited[indexes[i]]:
                    indexes[i] -= 1
                else:
                    visited[indexes[i]] = True
                    indexes[i] -= 1

                    break

    print(answer)