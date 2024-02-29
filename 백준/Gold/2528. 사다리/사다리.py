import sys

input = sys.stdin.readline

n, l = map(int, input().strip().split())

sadari = []
idx = n - 1

for _ in range(n):
    le, d = map(int, input().strip().split())
    if le == l:
        sadari.append([0, le, -1])
    elif d == 0:
        sadari.append([0, le, 0])
    else:
        sadari.append([l - le, l, 1])


# 길이와 전체길이가 똑같은 경우...
# 따로 처리

def sadariMove():
    # 부딛히면 변경
    for i, v in enumerate(sadari):
        if v[2] == 0:
            sadari[i][0] += 1
            sadari[i][1] += 1
        elif v[2] == 1:
            sadari[i][0] -= 1
            sadari[i][1] -= 1

    for i, v in enumerate(sadari):
        if v[2] == 0:
            if v[1] == l:
                sadari[i][2] = 1
        elif v[2] == 1:
            if v[0] == 0:
                sadari[i][2] = 0


def peopleMove():
    global idx

    while idx != 0:
        # if sadari[idx][0] <= sadari[idx - 1][0] <= sadari[idx][1] or sadari[idx][0] <= sadari[idx - 1][1] <= sadari[idx][1]:
        #     idx -= 1
        # else:
        #     break
        if sadari[idx][0] > sadari[idx - 1][1] or sadari[idx][1] < sadari[idx - 1][0]:
            break
        else:
            idx -= 1


def solve():
    answer = 0
    while True:
        peopleMove()
        if idx == 0:
            return answer
        sadariMove()
        answer += 1


print(solve())