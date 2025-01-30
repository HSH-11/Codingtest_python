def solution(s): 
    stack = []  
    for c in s:
        if stack and stack[-1] == "(" and c == ")":
            stack.pop()
        else:
            stack.append(c)
            
    if stack:
        return False
    else: 
        return True
    