from collections import Counter

def solution(weights):
    c = Counter(weights)
    w = set(weights)
    answer = 0
    
    for k in c:
        if c[k] > 1:
            answer += c[k] * (c[k] - 1) // 2
    for v in w:
        if v * (2 / 4) in w:
            answer += c[v * (2 / 4)] * c[v]
        if v * (3 / 4) in w:
            answer += c[v * (3 / 4)] * c[v]
        if v * (2 / 3) in w:
            answer += c[v * (2 / 3)] * c[v]
            
    return answer