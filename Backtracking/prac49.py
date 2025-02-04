def dfs(cur_k,cnt,dungeons,visited):
    answer = cnt
    for i in range(len(dungeons)):
        if cur_k >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            answer = max(answer,dfs(cur_k-dungeons[i][1],cnt+1,dungeons,visited))
            visited[i] = 0 #백트래킹을 위해서는 방문하지 않은 것처럼 간주해야 함
    
    return answer
            


def solution(k, dungeons):
    visited = [0] * len(dungeons)
    answer = dfs(k,0,dungeons,visited)
    
    return answer