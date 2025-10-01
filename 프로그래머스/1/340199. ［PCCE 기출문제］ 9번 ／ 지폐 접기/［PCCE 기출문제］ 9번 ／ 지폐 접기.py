def solution(wallet, bill):
    answer = 0
    
    while True:
        print(bill)
        # 지폐를 넣을수 있는가 
        if (bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[0] <= wallet[1] and bill[1] <= wallet[0]):
            break
            
        else:
            answer += 1
            if bill[0] > bill[1]:
                bill[0] = bill[0] // 2
            else:
                bill[1] = bill[1] // 2    
        
    
    return answer