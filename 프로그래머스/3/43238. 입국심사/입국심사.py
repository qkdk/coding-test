def solution(n, times):
    
    left = 0
    right = 1000000000 * 1000000000
    mid = (left + right) // 2
    target = n
    
    while left < right:
        tmp = 0
        for v in times:
            tmp += mid // v
        
        # 오른쪽으로
        if tmp < target:
            left = mid + 1
        else:
            right = mid
        
        mid = (right + left) // 2
        
    answer = left
    return answer

    