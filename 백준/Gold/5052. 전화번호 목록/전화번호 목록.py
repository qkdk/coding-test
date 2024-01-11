import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

class Node:
    def __init__(self, v):
        self.v = v
        self.children = {}
        self.endFlag = False


def bfs(rootNode):
    q = deque()
    q.append(rootNode)

    while q:
        curNode = q.popleft()
        print(curNode.v)

        for next in curNode.children:
            q.append(curNode.children[next])

for _ in range(tc):
    n = int(input())

    rootNode = Node(-1)
    flag = False

    lst = []
    for _ in range(n):
        lst.append(input().strip())

    lst.sort(key=lambda x:len(x))
    # print(lst)
    for line in lst:
        curNode = rootNode

        if not flag:
            for v in line:
                if curNode.endFlag:
                    print("NO")
                    flag = True
                    break
                if v in curNode.children:
                    curNode = curNode.children[v]
                else:
                    curNode.children[v] = Node(v)
                    curNode = curNode.children[v]
            curNode.endFlag = True

    if not flag:
        print("YES")