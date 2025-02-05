def solution(s):
    counts = [0] * 26
    for c in s:
        counts[ord(c)-ord('a')] += 1

    
    sorted_str = ""
    for i  in range(26):
        sorted_str += chr(i + ord("a")) * counts[i]

    return sorted_str


# TEST 코드
print(solution('hello')) # 반환값 : 'ehllo'
print(solution('algorithm')) # 반환값 : 'aghilmort'