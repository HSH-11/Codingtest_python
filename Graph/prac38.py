from collections import defaultdict

def solution(graph,start):
    #인접 리스트로 변환
    adj_list = defaultdict(list)
    #defaultdict클래스는 키가 없을 때 기본값을 defaultdict 형태로 기본값을 지정한다.
    for u, v in graph:
        adj_list[u].append(v)

    print(adj_list)

    def dfs(node, visited, result):
        visited.add(node) #현재 노드를 방문한 노드들의 집합에 추가
        result.append(node) #현재 노드를 결과 리스트에 추가
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, visited, result)
        
    
    visited = set()
    result = []
    dfs(start, visited, result)
    return result

# TEST 코드
print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A')) # 반환값 : ['A', 'B', 'C', 'D', 'E']
print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A')) # 반환값 : ['A', 'B', 'D', 'E', 'F', 'C']