def solution(name, yearning, photo):
    dic = {name[i] : yearning[i] for i in range(len(name))}

    answer = []
    
    for p in photo:
        score = 0
        for n in p:
            if n in dic:
                score += dic[n]
        answer.append(score)
                
    return answer