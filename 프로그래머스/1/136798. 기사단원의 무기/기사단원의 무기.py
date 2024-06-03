import math

def solution(number, limit, power):
    ans = []
    for n in range(1, number + 1):
        tmp = set()
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                tmp.add(i)
                tmp.add(n // i)
        if len(tmp) > limit:
            ans.append(power)
        else:
            ans.append(len(tmp))
    return sum(ans)