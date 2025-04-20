# 모든 시분을 초단위로 변환

def solution(video_len, pos, op_start, op_end, commands):
    video_len = convert(video_len)
    pos = convert(pos)
    op_start = convert(op_start)
    op_end = convert(op_end)
    
    for command in commands:
        if op_start <= pos <= op_end:
                pos = op_end
                
        if command == 'next':
            pos = min(pos + 10 ,video_len)
            
        elif command == 'prev':
            pos = max(0, pos - 10)
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    m = pos // 60 
    s = pos % 60
    a = format(m, '02')
    b = format(s, '02')
    # print(f"{a}:{b}")
    
    answer = f"{a}:{b}"
    return answer

def convert(string):
    m, s = map(int, string.split(":"))
    return m * 60 + s