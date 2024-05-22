def solution(words):
    tree = [{}, 0]
    
    for word in words:
        prev = tree
        for i in range(len(word)):
            cur = word[i]
            
            if cur not in prev[0]:
                prev[0][cur] = [{}, 0]
                
            prev[0][cur][1] += 1
            prev = prev[0][cur]
            
    answer = 0
    for word in words:
        count = 0
        prev = tree
        for i in range(len(word)):
            count += 1
            cur = word[i]
            if prev[0][cur][1] == 1:
                break
            prev = prev[0][cur]
        answer += count
        
    return answer