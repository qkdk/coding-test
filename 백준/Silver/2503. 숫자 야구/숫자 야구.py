import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

perm = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

for _ in range(n):
    num, s, b = input().split()
    s = int(s)
    b = int(b)
    
    i = 0
    while True:
        if i == len(perm):
            break
        sCount = 0
        bCount = 0

        for j in range(3):
            if num[j] == perm[i][j]:
                sCount += 1
            elif num[j] in perm[i]:
                bCount += 1

        if sCount != s or bCount != b:
            perm.remove(perm[i])
            i -= 1
        i += 1

print(len(perm))