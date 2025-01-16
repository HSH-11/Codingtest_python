def solution(N):
    stack = []
    while N > 0:
        remainder = N % 2
        stack.append(str(remainder))
        N //= 2 #O(logN)
    
    stack.reverse()
    return ''.join(stack) 

# TEST 코드
print(solution(10)) #반환값 :  1010
# print(solution(27)) #반환값 :  11011
# print(solution(12345)) #반환값 : 11000000111001