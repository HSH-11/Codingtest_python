def getAns(n,y,width,diagonal1,diagonal2):
    answer = 0
    if y == n: #y는 현재 위치가 결정된 퀸의 개수(즉, 조건 만족 경우의 수)
        answer += 1
    else:
        for i in range(n):
            #해당 위치에 이미 퀸이 있거나 대각선 상에 퀸이 있는 경우 스킵
            #인덱스를 이용해 대각선 귄 유무 판별
            if width[i] or diagonal1[i+y] or diagonal2[i-y+n]:
                continue      
            width[i] = diagonal1[i+y] = diagonal2[i-y+n] = True
            answer += getAns(n,y+1,width,diagonal1,diagonal2)
            width[i] = diagonal1[i+y] = diagonal2[i-y+n] = False
    return answer        
def solution(n):
    answer = getAns(n,0,[False] * n, [False] * (n * 2), [False] * (n * 2))
    return answer