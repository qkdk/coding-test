import sys

input = sys.stdin.readline

x = int(input())
line = input().strip()


# 주기 찾기


def findPeriod():
    global line
    st = set()
    st.add(line)
    count = 1
    while True:
        tmpLine = [0] * len(line)
        for i in range(0, len(line), 2):
            tmpLine[i // 2] = line[i]
        for i in range(1, len(line), 2):
            tmpLine[len(line) - 1 - i // 2] = line[i]

        line = ''.join(tmpLine)
        if line in st:
            break
        st.add(line)
        count += 1

    return count


def solve():
    global x, line

    period = findPeriod()
    target = x % period
    for i in range(target):
        tmpLine = [0] * len(line)
        for i in range(0, len(line), 2):
            tmpLine[i // 2] = line[i]
        for i in range(1, len(line), 2):
            tmpLine[len(line) - 1 - i // 2] = line[i]

        line = ''.join(tmpLine)

    return line


print(solve())