def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(cur_pos, opponent_pos):
        x, y = cur_pos
        
        # 현재 위치에 발판이 없으면 즉시 패배
        if board[x][y] == 0:
            return 0
        
        result = 0  # 최종 턴 수
        
        # 4방향으로 이동 시도
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 이동 불가능한 경우 스킵
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 0:
                continue
            
            # 현재 발판 제거하고 재귀 호출
            board[x][y] = 0
            next_turns = dfs(opponent_pos, (nx, ny)) + 1
            board[x][y] = 1  # 백트래킹
            
            # 전략적 선택
            if next_turns % 2 == 1 and result % 2 == 0:
                # 이번에 이길 수 있고, 지금까지 모두 진 경우
                result = next_turns
            elif next_turns % 2 == 0 and result % 2 == 0:
                # 모두 지는 경우: 최대한 오래 버티기
                result = max(result, next_turns)
            elif next_turns % 2 == 1 and result % 2 == 1:
                # 모두 이기는 경우: 최대한 빨리 승리
                result = min(result, next_turns)
        
        return result
    
    return dfs(aloc, bloc)
