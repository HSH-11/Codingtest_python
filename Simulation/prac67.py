def solution(brown, yellow):
    size = brown + yellow
    answer = []
    for i in range(3,int(size**0.5)+1):
        if (size % i == 0):
            x = size // i
            if (brown == (x+i)*2-4):
                answer.append(x)
                answer.append(i)
            
    return answer