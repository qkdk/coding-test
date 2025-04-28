def solution(schedules, timelogs, startday):
    startday -= 1
    count = 0
    tmp = []
    for v in schedules:
        tmp.append(convert_time(v))
        
    schedules = tmp
    
    answer = [True] * len(schedules)
    for _ in range(7):
        if not is_weekend(startday):
            for i in range(len(schedules)):
                crit = schedules[i]
                target = timelogs[i][count]
                
                if crit < target:
                    answer[i] = False
                    
        startday = (startday + 1) % 7
        count += 1
    
    
    a = 0
    for v in answer:
        if v:
            a += 1
    
    
    
    return a

def is_weekend(startday):
    if startday == 5 or startday == 6:
        return True
    return False

def convert_time(time):
    time += 10
    h = time // 100
    m = time % 100
    
    if m >= 60:
        m -= 60
        h += 1
        
    return h * 100 + m
        