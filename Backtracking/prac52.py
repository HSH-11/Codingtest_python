from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
        
    answer =  len(dist) + 1
    
    for i in range(length):
        for friends in permutations(dist,len(dist)):
            cnt = 1
            pos = weak[i] + friends[cnt-1]
            for j in range(i,i+length):
                if pos < weak[j]:#weak[i]는 시작점
                    cnt += 1
                    if cnt > len(dist):#모든 친구가 투입되었으면 해당 케이스 탐색 종료
                        break
                    pos = weak[j] + friends[cnt-1]
            answer = min(answer,cnt)
    return answer if answer <= len(dist) else -1