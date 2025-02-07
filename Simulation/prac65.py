def solution(s):
    cnt_trans = 0
    cnt_zero = 0
    
    while s != "1":
        cnt_trans += 1
        cnt_zero += s.count("0")
        s = bin(s.count("1"))[2:]
        
    answer = [cnt_trans,cnt_zero]
    return answer