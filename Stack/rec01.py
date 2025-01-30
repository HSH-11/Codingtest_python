def solution(arr):
    answer = []
    answer.append(arr[0])
    n = len(arr)
    for i in range(1,n):
        if (answer[-1] == arr[i]):
            continue
        else:
            answer.append(arr[i])
    return answer