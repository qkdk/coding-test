import sys

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(input().split())

def solve():
    answer = []
    alphaSet = set()

    for words in lst:
        # 단어의 첫글자 확인
        if not checkFirstChar(alphaSet, words):
            # 단어 처음부터 탐색하면서 파악하기
            flag = False
            for i, word in enumerate(words):
                if flag:
                    break
                for j, c in enumerate(word):
                    if c.upper() not in alphaSet:
                        alphaSet.add(c.upper())
                        words[i] = word[0:j] + '[' + word[j] + ']' + word[j + 1:]

                        flag = True
                        break

def checkFirstChar(alphaSet, words):
    flag = False
    for i, word in enumerate(words):
        if word[0].upper() not in alphaSet:
            alphaSet.add(word[0].upper())
            words[i] = '[' + word[0] + ']' + word[1:]

            flag = True
            break
    return flag


solve()
for words in lst:
    for word in words:
        print(word, end=' ')
    print()