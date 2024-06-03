from collections import deque

def solution(n, m, section):
    answer = 0
    q = deque(section)
    
    while q:
        answer += 1
        v = q.popleft()
        left = v
        right = v + m - 1
        
        while q:
            if left <= q[0] <= right:
                q.popleft()
            else:
                break
        
    return answer