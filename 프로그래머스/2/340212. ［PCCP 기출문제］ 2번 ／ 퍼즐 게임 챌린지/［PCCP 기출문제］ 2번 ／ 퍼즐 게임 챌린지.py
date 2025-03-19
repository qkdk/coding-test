from dataclasses import dataclass

@dataclass
class Test:
    a : int = 10

def solution(diffs, times, limit):

    # 여기서 현재 탐색할 level 지정
    min_level = 1
    max_level = 100000
    
    while min_level < max_level:
        cur_level = (min_level + max_level) // 2
        
        sum = 0
        for i in range(0, len(times)):
            sum += cc(cur_level, diffs[i], times[i], times[i - 1])
            
        if sum > limit:
            # 레벨을 늘려야함
            min_level = cur_level + 1
        else:
            max_level = cur_level 
        
    return min_level


# 1일때 2일때 3일때... limit일때
def cc(level, diff, cur_time, prev_time):
    if level >= diff:
        return cur_time
    else:
        return (diff - level) * (cur_time + prev_time) + cur_time
    