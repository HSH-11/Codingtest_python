def solution(array, commands):
    answer = []
    for com in commands:
        sub = array[com[0]-1:com[1]]
        sub.sort()
        answer.append(sub[com[2]-1])
    return answer