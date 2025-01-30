def solution(s):
    arr = s.split(" ")
    answer = 0
    for i in range(len(arr)):
        if not arr[i] == "Z":
            answer += int(arr[i])
        else:
            answer -= int(arr[i-1])
    return answer