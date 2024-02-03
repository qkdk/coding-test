import sys

input = sys.stdin.readline

n = int(input())
length = n // 5
count = length // 4

line = input().strip()

matrix = []
for i in range(5):
    matrix.append('.' + line[i * length: (i + 1) * length])

length += 1

checkNumber = [
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)],
    [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 2), (4, 0), (4, 1), (4, 2)],
    [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)]
]

for v in checkNumber:
    v.sort()


def solve():
    answer = []
    for k in range(0, length):
        tmpLst = []
        for y in range(0, 5):
            for x in range(0, 3):
                nx = k + x
                if nx >= length:
                    break
                if matrix[y][nx] == '#':
                    tmpLst.append((y, x))
        for i, v in enumerate(checkNumber):
            if v == tmpLst:
                answer.append(str(i))

    return ''.join(answer)


print(solve())