def solution(board):
    #좌표 이탈 체크
    def is_valid(x,y):
        return 0 <= x < N and 0 <=y < N
    #이동할 수 없는 영역 체크
    def is_blocked(x,y):
        return (x, y) == (0,0) or not is_valid(x,y) or board[x][y] == 1
    #비용은 방향에 따라 결정
    def calculate_cost(direction, prev_direction, cost):
        #prev_direction == -1은 아직 방향이 정해지지 않은 초기 상태
        if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
            return cost + 100
        else:
            return cost + 600
        
    def isShouldUpdate(x,y,direction, new_cost):
        return visited[x][y][direction] == 0 or visited[x][y][direction] > new_cost
    
    queue = [(0,0,-1,0)]
    N = len(board)
    directions = [(0,-1),(-1,0),(0,1),(1,0)]
    #x,y위치에서 이동할 수 있는 방향의 비용 저장
    visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    answer = float("inf")
    
    while queue:
        x,y,prev_direction,cost = queue.pop(0)
        
        for direction, (dx,dy) in enumerate(directions):
            new_x, new_y = x+dx,y+dy
            
            if is_blocked(new_x,new_y):
                continue
                
            new_cost = calculate_cost(direction,prev_direction,cost)
            
            if (new_x,new_y) == (N-1,N-1):
                answer = min(answer, new_cost)
            elif isShouldUpdate(new_x,new_y,direction,new_cost):
                queue.append((new_x,new_y,direction,new_cost))
                visited[new_x][new_y][direction] = new_cost
                
    return answer