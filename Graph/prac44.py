import heapq #현재까지 선택하지 않은 노드 중 최소 비용 값이 최소인 노드를 선택하기 위해 cost를 기준으로 오름차순 정렬하는 heapq 사용

def solution(N, road, K):
    #각 노드에 연결된 간선들을 저장할 리스트
    graph = [[] for _ in range(N + 1)]
    #출발점에서 각 노드까지의 최단 거리를 저장할 리스트
    distances = [float("inf")] * (N + 1)
    distances[1] = 0
    
    #그래프 구성(양방향 고려)
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        
    heap = []
    heapq.heappush(heap, (0, 1)) #출발점을 heap에 추가
    while heap:
        dist, node = heapq.heappop(heap)
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    print(distances)
    return sum(1 for dist in distances if dist <= K)
                