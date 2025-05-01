'''
모든 지점 좌표 변환
for 문으로 1초 이동 구현
matrix에 위치 표시 0 기본값
1. 시작하자마자 겹치는 것이 있는지 확인
2. 확인 후 겹치는 부분 다 제거
3. 도달 끝난 애들 제거
    * 각 애들별로 도달한 갯수 저장
    * 이거 활용해서 끝나는것과 다음 지점 목표 파악
4. 애들 위치는 list로 가지고 있는다
'''

def solution(points, routes):
    # 전처리
    cur_pos = []
    cur_idxs = [0] * len(routes)
    
    dests = []
    for route in routes:
        dest_per_vertex = []
        for vertex in route:
            dest_per_vertex.append(points[vertex - 1])
        
        dests.append(dest_per_vertex)
    matrix = init_matrix()
    for dest in dests:
        cur_pos.append(dest[0])
        matrix[dest[0][0]][dest[0][1]] += 1
    
    # 끝난애들 확인
    endcount = 0
    answer = 0    
    while endcount < len(routes):
        answer += check_matrix(matrix)
        matrix = init_matrix()
        
        # 각 점 마다 현재 위치와 도달위치를 비교
        # 현재위치와 전체 길이가 같다면 continue
        # 같다면 인덱스 + 1
        # 인덱스 + 1 했을때 전체 길이와 같다면 endcount + 1
        for i in range(len(routes)):
            cur_idx = cur_idxs[i]
            if cur_idx == len(routes[0]):
                continue
            if cur_pos[i] == dests[i][cur_idx]:
                cur_idxs[i] += 1
                if cur_idxs[i] == len(routes[0]):
                    endcount += 1
                    continue
                    
            by, bx = move(cur_pos[i], dests[i][cur_idxs[i]])
            matrix[by][bx] += 1
            cur_pos[i] = [by, bx]
    return answer

def check_current_coord():
    pass

vector = [[-1,0],[1,0],[0,1],[0,-1]]
def move(cur_pos, dest_pos):
    cy, cx = cur_pos
    ty, tx = dest_pos
    ay, ax = 0,0
    min_dist = float('inf')
    for dy, dx in vector:
        ny, nx = cy + dy, cx + dx
        dist = abs(ny - ty) + abs(nx - tx)
        if dist < min_dist:
            min_dist = dist
            ay, ax = ny, nx
    
    return ay, ax 
    

def check_matrix(matrix):
    count = 0
    for row in matrix:
        for v in row:
            if v > 1:
                count += 1

    return count

def init_matrix():
    return [[0] * 101 for _ in range(101)]

                