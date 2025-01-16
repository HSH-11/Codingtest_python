def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                pick = j[i-1]
                j[i-1] = 0
                if stack and pick == stack[-1]:
                    stack.pop()
                    answer += 2
                    break
                else:
                    stack.append(pick)
                    break
    print(answer)
    return answer