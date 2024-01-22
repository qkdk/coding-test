import sys

input = sys.stdin.readline

n = int(input())


class Pair:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return str(self.start) + " " + str(self.end)


timeLst = []
for _ in range(n):
    a, b = map(int, input().split())
    timeLst.append(Pair(a, b))

timeLst.sort(key=lambda x: (x.end, x.start))
endTime = 0
answer = 0

for time in timeLst:
    if time.start >= endTime:
        endTime = time.end
        answer += 1

print(answer)