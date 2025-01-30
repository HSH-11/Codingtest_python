def solution(msg):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Index = {c: i + 1 for i, c in enumerate(Alphabet)}
    
    w = ""
    answer = []
    for c in msg:
        wc =  w + c
        if wc in Index.keys(): #사전에서 현재 입력과 일치하는 가장 긴 문자열 찾기
            w = wc #w를 wc로 갱신
        else:
            answer.append(Index[w]) #추가하기 이전까지의 w 색인 번호 추가
            Index[wc] = len(Index)+1 #사전 추가
            w = c #w는 새로 시작하는 c로 경신
            
    if w: #마지막 남은 w을 추가
        answer.append(Index[w])
             
    return answer