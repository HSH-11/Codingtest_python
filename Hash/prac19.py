def polynomial_hash(str): #O(1)
    p =31
    m = 1_000_000_007
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p +ord(char)) % m
    
    return hash_value


def solution(string_list, query_list):

    hash_list = [polynomial_hash(str) for str in string_list] #O(N)

    result = []
    for query in query_list: #O(K)
        query_hash = polynomial_hash(query)
        if query_hash in hash_list:
            result.append(True)
        else:
            result.append(False)

    return result #O(N+K)

# TEST 코드
print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"] )) # 반환값 : [True, False, False, True]