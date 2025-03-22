def print_matrix(matrix):
    for row in matrix:
        print(row)

import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
result = list(input().strip())

matrix = []
q_index = 0
for i in range(n):
    lst = list(input().strip())
    matrix.append(lst)
    if lst[0] == '?':
        q_index = i

prev_matrix = matrix[:q_index]
start_list = [chr(ord('A') + i) for i in range(k)]
post_matrix = matrix[q_index + 1:]
post_matrix.reverse()

def play_game(matrix, pos):
    for j in range(len(matrix)):
        for i in range(len(pos) - 1):
            if matrix[j][i] == '-':
                pos[i], pos[i + 1] = pos[i + 1], pos[i]

    return pos

prev_r = play_game(prev_matrix, start_list)
post_r = play_game(post_matrix, result)

error = 'x' * (k - 1)
answer = ""

for i in range(len(prev_r) - 1):
    # 하나라도 맞으면 *
    # 바꿔서 되면 -
    # 바꿔도 안되면 error
    if prev_r[i] == post_r[i]:
        answer += "*"
    elif prev_r[i] == post_r[i + 1] and prev_r[i + 1] == post_r[i]:
        answer += "-"
        prev_r[i], prev_r[i + 1] = prev_r[i + 1], prev_r[i]
        # print(prev_r)
    else:
        print(error)
        exit()

print(answer)

