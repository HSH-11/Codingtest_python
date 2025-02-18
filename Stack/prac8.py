def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)

        elif c == ')':
            if not stack:
                return False
            else:
                stack.pop()
    
    if stack:
        return False
    else:
        return True

        

# TEST 코드
print(solution('(())()')) # 반환값 : True
print(solution('((())()')) # 반환값 : False