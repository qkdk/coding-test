import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
lst.sort()

idx = int(len(lst) / 2)

def method_name(idx):
    answer = 0

    for i in range(len(lst)):
        answer += abs(lst[i] - lst[idx])
    return answer


if method_name(idx) < method_name(idx - 1):
    print(lst[idx])
else:
    print(lst[idx - 1])