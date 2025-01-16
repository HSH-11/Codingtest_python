def solution(record):
    answer = []
    user_id = {}
    
    for line in record:
        cmd = line.split(" ")
        if cmd[0] != "Leave":
            user_id[cmd[1]] = cmd[2]
    
    for line in record:
        cmd = line.split(" ")
        if cmd[0] == "Enter":
            answer.append(f"{user_id[cmd[1]]}님이 들어왔습니다.")
        elif cmd[0] == "Change":
            pass
        else:
            answer.append(f"{user_id[cmd[1]]}님이 나갔습니다.")
    return answer