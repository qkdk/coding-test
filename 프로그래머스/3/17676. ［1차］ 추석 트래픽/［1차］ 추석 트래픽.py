def solution(lines):
    times = []
    for line in lines:
        sp = line.split(" ")
        
        tmp = list(map(float,sp[1].split(":")))
        endTime = int((tmp[0] * 3600 + tmp[1] * 60 + tmp[2]) * 1000)
        dur = int(float(sp[2][:-1]) * 1000)
        startTime = endTime - dur + 1
        time = [startTime, endTime]
        times.append(time)
        
    times.sort(key = lambda x: x[1])
    answer = 1
    for i in range(len(times)):
        cur = times[i]
        flag = cur[1] + 1000
        count = 1
        for j in range(i + 1, len(times)):
            tt = times[j]
            if tt[1] < flag or tt[0] < flag:
                count += 1
                
        answer = max(answer, count)
    
    return answer