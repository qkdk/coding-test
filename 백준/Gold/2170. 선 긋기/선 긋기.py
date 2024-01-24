import sys

input = sys.stdin.readline
n = int(input())

END = 1
START = 0

lst = []
q = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort()

answer = lst[0][END] - lst[0][START]
maxValue = lst[0][END]

for v in lst[1:]:
    start, end = v

    if maxValue <= start:
        answer += end - start
        maxValue = max(maxValue, end)
    else:
        if maxValue < end:
            answer += end - maxValue
            maxValue = end

print(answer)
'''
1. 시작순 정렬
2. 끝점들을 하나씩 모은다. (우선순위 큐)
3. 가장 큰 끝점이 내 시작점보다 작거나 같다면 -> 그냥 나의 길이 +
4. 아니라면
    가장 큰 끝점이 나의 끝점보다 작다면? 내 끝점 - 가장큰 끝점 +
    가장 큰 끝점이 나의 끝점보다 크다면 -> 무시
'''