def solution(graph, source):
    num_vertices = len(graph)

    distance = [float("inf")] * num_vertices
    distance[source] = 0

    #직전 경로 배열 초기화
    predecessor = [None] * num_vertices

    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]: #graph[u]는 u에서 출발하는 간선들의 리스트
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    #직전 경로 업데이트
                    predecessor[v] = u

    #음의 가중치 순회 체크
    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                #음의 가중치 순회가 발견되었으므로 [-1]을 반환.
                return [-1]
    
    return [distance, predecessor]

# TEST 코드
print(solution([[(1, 4), (2, 3), (4, -6 )], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)],[(2, 2)]],0)) #반환갑 : [[0, -2, -4, 3, -6], [None, 2, 4, 1, 0]]
print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]],0)) # 반환값 : [-1]
