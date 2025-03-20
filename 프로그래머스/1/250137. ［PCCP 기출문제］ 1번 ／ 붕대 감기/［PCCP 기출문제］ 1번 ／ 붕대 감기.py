def update(init_health, health, plus):
    if health + plus > init_health:
        return init_health
    return health + plus

def solution(bandage, health, attacks):
    max_time = max(attacks, key =lambda x: x[0])[0]
    
    init_health = health
    dict = {}
    for i, v in attacks:
        dict[i] = v
    
    conti = 0    
    for i in range(1, max_time + 1):
        if i in dict:
            health -= dict[i]
            if health <= 0:
                return -1
            conti = 0
            
            continue
        
        conti += 1
        
        if conti == bandage[0]:
            health = update(init_health, health, bandage[2] + bandage[1])
            conti = 0
        else:
            health = update(init_health, health, bandage[1])
            
            
    return health