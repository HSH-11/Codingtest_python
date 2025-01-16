from collections import defaultdict, deque

def solution(graph, start):

    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    print(adj_list)

    def bfs(start):
        visited = set()

        queue = deque([start])
        visited.add(start)
        result.append(start)

        while queue:  
            node = queue.popleft()  # 큐에 있는 원소 중 가장 먼저 푸시된 원소 팝
            for neighbor in adj_list.get(node, []):  #인접한 이웃 노드들에 대해서
                if neighbor not in visited:  #  방문되지 않은 이웃 노드인 경우
                    # 이웃노드를 방문 처리함
                    queue.append(neighbor)
                    visited.add(neighbor)  
                    result.append(neighbor)

    result = []
    bfs(start)
    return result

# TEST 코드
print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)],1)) # 반환값 :[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)],1)) # 반환값 : [1, 2, 3, 4, 5, 0]