from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)  # 현재 다리를 건너는 트럭 (deque로 사용)
    total_weight = 0  # 다리 위의 트럭들의 총 무게
    
    while truck_weights:  # 트럭이 다리를 다 건널 때까지 반복
        answer += 1
        total_weight -= bridge.popleft()  # 다리에서 트럭 하나 빼기 (무게 차감)
        
        if total_weight + truck_weights[0] <= weight:  # 트럭이 다리를 건널 수 있는지 확인
            truck = truck_weights.pop(0)  # 트럭을 빼서
            bridge.append(truck)  # 다리에 추가
            total_weight += truck  # 트럭 무게 추가
        else:
            bridge.append(0)  # 트럭이 지나갈 수 없으면 빈 공간 추가
    
    # 마지막 트럭이 다리 끝에 도달했을 때 시간을 더해주기
    return answer + bridge_length
