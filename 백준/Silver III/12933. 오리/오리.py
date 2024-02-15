import sys

input = sys.stdin.readline

line = input().strip()

dic = {'q': 0, 'u': 0, 'a': 0, 'c': 0, 'k': 0}


def solve():
    answer = 0

    for v in line:
        if v == 'q':
            dic['q'] += 1
        elif v == 'u':
            if dic['q'] == dic['u']:
                return -1
            else:
                dic['u'] += 1
        elif v == 'a':
            if dic['u'] == dic['a']:
                return -1
            else:
                dic['a'] += 1
        elif v == 'c':
            if dic['a'] == dic['c']:
                return -1
            else:
                dic['c'] += 1
        elif v == 'k':
            if dic['c'] == dic['k']:
                return -1
            else:
                answer = max(answer, dic['q'])
                dic['q'] -= 1
                dic['u'] -= 1
                dic['a'] -= 1
                dic['c'] -= 1

    std = dic['q']
    for v in dic.values():
        if std != v:
            return -1

    return answer


print(solve())