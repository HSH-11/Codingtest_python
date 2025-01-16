"""def solution(prices): O(N^2)
    n = len(prices)
    answer = [0] * n
    for i in range(n):
        if i == n-1:
            break
        for j in range(i+1,n):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break         
    return answer"""

def solution(prices):
    n =  len(prices)
    answer = [0] * n
    
    stack = [0]
    for i in range(1,n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    
    return answer