import heapq
#오름차순으로 pop을 하는 heapq의 특성을 이용하면 선택되지 않은 노드 중 최소 비용이 가장 적은 노드를 pop 가능
def solution(graph, start):
    distances = {node: float("inf") for node in graph} #모든 노드의 거리 값 무한대로 초기화
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start]) #시작 노드를 큐에 삽입
    paths = {start: [start]} #최단 경로 저장

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        #만약 현재 노드의 거리 값이 큐에서 가져온 거리 값보다 크면, 해당 노드는 이미 처리한 것이므로 무시
        if distances[current_node] < current_distance:
            continue

        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance # 최소 비용 업데이트
                paths[adjacent_node] = paths[current_node] + [adjacent_node] #최단 경로 업데이트
                #최소 경로가 갱신된 노드를 비용과 함께 큐에 푸시
                heapq.heappush(queue, [distance, adjacent_node])
    
    #paths 딕셔너리를 노드 번호에 따라 오름차순으로 정렬하여 변환
    sorted_paths = {node: paths[node] for node in sorted(paths)}

    return [distances, sorted_paths]

# TEST 코드
print(solution({ 'A': {'B': 9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1} },'A')) # 반환값 :[{'A': 0, 'B': 4, 'C': 3}, {'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C']}]
print(solution({'A': {'B': 1},'B': {'C': 5},'C': {'D': 1},'D': { } }, 'A')) # 반환값 :[{'A': 0, 'B': 1, 'C': 6, 'D': 7}, {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D']}]