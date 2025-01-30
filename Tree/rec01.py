#입국 심사 문제
def solution(n, times):
    left = min(times)
    right = max(times) * n
    answer = right  # 최댓값을 초기 정답으로 설정
    
    while left <= right:
        mid = (left + right) // 2  # 중간값울 기준으로 시간 안에 n명을 심사할 수 있는 지 확인
        
        # mid 시간 동안 심사할 수 있는 총 인원 계산
        people = sum(mid // time for time in times)

        if people >= n:  # n명을 모두 처리할 수 있다면
            answer = mid  # 정답 후보 갱신
            right = mid - 1  # 시간을 더 줄여서 최소 시간 찾기
        else:
            left = mid + 1  # 시간이 부족하므로 시간을 늘리기
    return answer