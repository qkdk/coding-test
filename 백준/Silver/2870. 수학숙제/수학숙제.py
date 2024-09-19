import sys

input = sys.stdin.readline

n = int(input())

answer = []
for _ in range(n):
    line = str(input())
    index = 0

    tmp = ""
    while index < len(line):
        if line[index].isdigit():
            tmp += line[index]
        else:
            if tmp != "":
                answer.append(int(tmp))
            tmp = ""

        index += 1

answer.sort()
print(' '.join(map(str, answer)))