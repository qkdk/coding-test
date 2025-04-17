# 초기 서버는 1개고, 수용가능한 인원은 m
# 수용가능한 인원 m + 1 일때, 필요서버는 2
# 필요서버 구하는 공식은 인원수 // m + 1


def solution(players, m, k):
    servers = [0] * 100
    cur_servers = 1
    answer = 0
    
    for i in range(len(players)):
        need = players[i] // m + 1
        
        if need > cur_servers:
            add = need - cur_servers
            cur_servers += add
            servers[i + k - 1] += add
            answer += add
            
        cur_servers -= servers[i]
        
    return answer