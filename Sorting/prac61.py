from heapq import heappush, heappop
def isValid(N,x,y):
    return 0<=x<N and 0<=y<N
def solution(land, height): # 이동할 수 있는 칸 중 가작 작은 차이가 나는 곳부터 방문=> 힙을 이용해 정렬
    n = len(land[0])
    answer = 0
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    visited = [[False] * n for _ in range(n)]
    q = []
    heappush(q,[0,0,0])
    
    while q:
        cost, y, x = heappop(q)
        if not visited[y][x]:
            visited[y][x] = True
            answer += cost
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if(isValid(n,ny,nx)):
                    temp_cost = abs(land[y][x]-land[ny][nx])
                    if temp_cost > height:
                        new_cost = temp_cost
                    else:
                        new_cost = 0 #사다리가 놓이지 않은 곳
                    heappush(q,[new_cost, ny, nx])
    
    return answer