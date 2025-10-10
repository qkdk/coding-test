from itertools import combinations_with_replacement

def solution(n, info):
    scores = [10,9,8,7,6,5,4,3,2,1,0]
    results = list(combinations_with_replacement(scores, n))
    max_score = 0
    answer = [-1]
    
    for result in results:
        
        gets = [0] * 11
        for r in result:
            gets[r] += 1
        
        l_score = 0
        p_score = 0
        for i in range(len(info)):
            peach = info[i]
            lion = gets[i]
            
            if lion == 0 and peach == 0:
                continue
                
            elif lion > peach:
                l_score += (10 - i)
            else:
                p_score += (10 - i)
                
        diff = l_score - p_score
        
        if max_score < diff:
            max_score = diff
            answer = gets
            
    return answer