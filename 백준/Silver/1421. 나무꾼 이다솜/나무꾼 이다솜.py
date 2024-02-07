import sys

input = sys.stdin.readline

n, c, w = map(int, input().split())

woods = []
for _ in range(n):
    woods.append(int(input()))

answer = 0
for i in range(1, max(woods) + 1):

    sumPrice = 0

    for v in woods:
        piece = 0
        count = 0

        a = v // i
        b = v % i

        if a != 0 and b != 0:
            count += a
            piece += a
        elif a != 0 and b == 0:
            count += a - 1
            piece += a

        price = piece * i * w - count * c
        if price < 0:
            continue
        sumPrice += price

    answer = max(answer, sumPrice)

print(answer)