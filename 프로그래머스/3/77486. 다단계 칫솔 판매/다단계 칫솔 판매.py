# 꼭 끝에서 할 필요는 없다.
# 그냥 수익 나면 항상 위로 쭉쭉 올라가게만 하면된다.
# 부모를 찾는걸 어케해야할까.?
# 부모 1차원 배열 이용해서 하면될듯
# 스트링을 숫자로 변경해주는 테이블 필요

def solution(enroll, referral, seller, amount):
    table = {}
    for i, v in enumerate(enroll):
        table[v] = i + 1
    
    parents = [-1] * (len(enroll) + 1)
    for i, v in enumerate(referral):
        if v == '-':
            parents[i + 1] = 0
            continue
        parents[i + 1] = table[v]
    
    result = [0] * (len(enroll) + 1)
    for i in range(len(seller)):
        n = table[seller[i]]
        v = amount[i] * 100
        tax = v // 10
        result[n] += v
        # 부모 찾아가면서 세금 납부
        findParents(n, parents, tax, result)
    
    return result[1:]

def findParents(n, parents, tax, result):
    if parents[n] == -1:
        return
    
    result[parents[n]] += tax
    result[n] -= tax
    if tax < 10:
        return
    findParents(parents[n], parents, tax // 10, result)