postResult = []
preResult = []

import sys
sys.setrecursionlimit(10**6)


def solution(nodeinfo):
    global postResult, preResult
    tree = {}
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
        tree[i + 1] = []
    sortedNode = sorted(nodeinfo)

    maxV = max(sortedNode, key=lambda x:x[1])
    dfs(sortedNode, 0, len(sortedNode), maxV, tree)
    
    postOrder(tree, maxV[2])
    preOrder(tree, maxV[2])
    answer = [preResult, postResult]
    
    return answer

def dfs(lst, left, right, cur, tree):
    if len(lst) == 0:
        return
    # 현재를 기준으로 두부류로 나누기
    idx = lst.index(cur)
    
    leftLst = lst[:idx]
    rightLst = lst[idx + 1:]

    if leftLst:
        maxV = max(leftLst, key=lambda x: x[1])
        tree[cur[2]].append(maxV[2])
        dfs(leftLst, left, idx, maxV, tree)
    if rightLst:
        maxV = max(rightLst, key=lambda x: x[1])
        tree[cur[2]].append(maxV[2])
        dfs(rightLst, left, idx, maxV, tree)

def postOrder(tree, node):
    global postResult
    
    for v in tree[node]:
        postOrder(tree, v)
        
    postResult.append(node)
    
def preOrder(tree, node):
    global preResult
    preResult.append(node)
    
    for v in tree[node]:
        preOrder(tree, v)

    
    