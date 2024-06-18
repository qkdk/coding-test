import sys

input = sys.stdin.readline

while True:
    m = int(input())
    if m == 0:
        break

    line = input().strip()

    li = 0
    ri = 0
    tmp = {}
    answer = 0

    # ri 의 값을 추가한다.
    # 만약에 갯수를 초괴한다면 li의 값을 지우고 li + 1
    # 그렇지 않다면 ri + 1
    while ri < len(line):
        if line[ri] in tmp:
            tmp[line[ri]] += 1
        else:
            tmp[line[ri]] = 1

        while len(tmp) > m:
            tmp[line[li]] -= 1
            if tmp[line[li]] == 0:
                tmp.pop(line[li])
            li += 1
        ri += 1

        answer = max(answer, ri - li)

    print(answer)