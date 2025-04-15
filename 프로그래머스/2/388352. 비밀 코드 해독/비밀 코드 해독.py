# 다섯자리로 가능한 모든 경우 탐색 (조합을 이용해서 만들면 된다.)
# m조건 만족하는지 반복문으로 판단
gq, gans, answer = 0,0,0

def solution(n, q, ans):
    global gq, gans, answer
    gq = q
    gans = ans
    
    dfs([0] * 5, 0, 0, n)
    return answer

def dfs(result, index, cur_value, max_value):
    if index == len(result):
        check(result)
        return
    
    # cur_value 보다 큰 값을 찾아야 한다.
    for value in range(cur_value + 1, max_value + 1):
        result[index] = value
        dfs(result, index + 1, value, max_value)

def check(result):
    global answer, gq, gans
    
    for lst, a in zip(gq, gans):
        count = 0
        
        for v in lst:
            if v in result:
                count += 1
                
        if count != a:
            return
    
    answer += 1

    