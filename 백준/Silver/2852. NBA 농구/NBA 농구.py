import sys

input = sys.stdin.readline


def calTime(time: str):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def calTimeR(time: int):
    return '{0:02d}:{1:02d}'.format(time // 60, time % 60)


def solve():
    n = int(input())
    lst = []
    for _ in range(n):
        team, time = input().split()
        lst.append((int(team), calTime(time)))
    lst.sort(key=lambda x: x[1])

    time = [0, 0, 0]
    score = [0, 0, 0]
    pTeam = 0
    pTime = 0

    for i, v in enumerate(lst):
        if v[0] == 1:
            score[1] += 1
            if score[1] > score[2] and pTeam == 0:
                pTeam = 1
                pTime = v[1]
            elif score[1] == score[2] and pTeam == 2:
                pTeam = 0
                time[2] += v[1] - pTime
        else:
            score[2] += 1
            if score[1] < score[2] and pTeam == 0:
                pTeam = 2
                pTime = v[1]
            elif score[1] == score[2] and pTeam == 1:
                pTeam = 0
                time[1] += v[1] - pTime

    if pTeam == 1:
        time[1] += 48 * 60 - pTime
    elif pTeam == 2:
        time[2] += 48 * 60 - pTime
    return calTimeR(time[1]), calTimeR(time[2])


t1, t2 = solve()
print(t1)
print(t2)