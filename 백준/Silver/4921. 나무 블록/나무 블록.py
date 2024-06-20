import sys

input = sys.stdin.readline

# 각 숫자 뒤에 올수있는 숫자를 dict

dic = {}
dic[1] = {4, 5}
dic[2] = {}
dic[3] = {4, 5}
dic[4] = {2, 3}
dic[5] = {8}
dic[6] = {2, 3}
dic[7] = {8}
dic[8] = {6, 7}

count = 1
while True:
    n = input().strip()
    if n == "0":
        break
    lst = list(map(int, n))

    flag = False
    if lst[0] == 1 and lst[-1] == 2:
        for i in range(len(lst) - 1):
            if lst[i + 1] in dic[lst[i]]:
                continue
            else:
                flag = True
                break
    else:
        flag = True

    if flag:
        print(str(count) + ". "  "NOT")
    else:
        print(str(count) + ". "  "VALID")

    count += 1