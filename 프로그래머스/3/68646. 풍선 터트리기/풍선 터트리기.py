# 한 점을 기준으로 좌 우를 봤을때, 둘다 한 점보다 작다면 불가능
# 하나만 작다면 가능
# 결국엔 좌와 우를 봐야하는데

def solution(a):
    leftMin = [0] * len(a)
    rightMin = [0] * len(a)
    
    minV = float('inf')
    for i in range(len(a)):
        if a[i] < minV:
            minV = a[i]
        leftMin[i] = minV
        
    minV = float('inf')
    for i in range(len(a)-1, -1, -1):
        if a[i] < minV:
            minV = a[i]
        rightMin[i] = minV
        
    count = 0
    for i in range(len(a)):
        lv = float('inf')
        rv = float('inf')
        if i - 1 >= 0:
            lv = leftMin[i - 1]
        if i + 1 < len(a):
            rv = rightMin[i + 1]
            
        curV = a[i]
        if lv < curV and rv < curV:
            continue
        else:
            # print(curV)
            # print(lv, rv)
            count += 1
        
        
    return count