def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:#반드시 양쪽이 연결되어 있음을 표시
        graph[a].append(b) 
        graph[b].append(a)
        
    def dfs(node, parent):
        cnt = 1
        for child in graph[node]:
            if child != parent:
                cnt += dfs(child,node)
        return cnt
    
    diff = float("inf")
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        cnt_a = dfs(a,b)
        cnt_b = n - cnt_a
        
        diff = min(diff, abs(cnt_a - cnt_b))
        
        graph[a].append(b)
        graph[b].append(a)
        
    return diff