import sys

input = sys.stdin.readline

n = int(input())


def solve():
    answer = []

    if n == 2:
        answer.append(1)
        answer.append(1)
    else:
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().strip().split())))

        a = (matrix[0][1] + matrix[0][2] - matrix[1][2]) // 2

        answer.append(a)
        for v in matrix[0][1:]:
            answer.append(v - a)

    return list(map(str, answer))


print(' '.join(solve()))